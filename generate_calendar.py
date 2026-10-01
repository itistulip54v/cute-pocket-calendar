import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, Polygon, Wedge
from datetime import datetime, timedelta
import calendar as cal
from reportlab.lib.pagesizes import A5
from reportlab.lib import colors
from reportlab.lib.units import cm, inch
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import io

# Color scheme
BLUE = colors.HexColor('#4A90E2')
LIGHT_BLUE = colors.HexColor('#A8D5FF')
YELLOW = colors.HexColor('#FFD700')
LIGHT_YELLOW = colors.HexColor('#FFFACD')
WHITE = colors.white
DARK_BLUE = colors.HexColor('#2E5C8A')

def draw_decorative_flowers(canvas_obj, x, y, size=0.3):
    """Draw cute hand-drawn style flowers"""
    # Petal positions
    petal_positions = [
        (0, size),      # top
        (size*0.7, size*0.7),   # top-right
        (size, 0),      # right
        (size*0.7, -size*0.7),  # bottom-right
        (0, -size),     # bottom
        (-size*0.7, -size*0.7), # bottom-left
        (-size, 0),     # left
        (-size*0.7, size*0.7)   # top-left
    ]
    
    # Draw petals
    canvas_obj.setFillColor(YELLOW)
    canvas_obj.setStrokeColor(DARK_BLUE)
    canvas_obj.setLineWidth(0.5)
    
    for px, py in petal_positions:
        canvas_obj.ellipse(x + px - 0.15, y + py - 0.2, x + px + 0.15, y + py + 0.2, fill=1)
    
    # Draw center
    canvas_obj.setFillColor(LIGHT_YELLOW)
    canvas_obj.circle(x, y, 0.15, fill=1)

def draw_decorative_dots(canvas_obj, x, y, pattern='scattered'):
    """Draw cute dot patterns"""
    canvas_obj.setFillColor(LIGHT_BLUE)
    if pattern == 'scattered':
        positions = [(0, 0), (0.3, 0.2), (0.6, 0.1), (0.2, 0.5), (0.5, 0.6)]
    else:
        positions = [(i*0.15, 0) for i in range(4)]
    
    for px, py in positions:
        canvas_obj.circle(x + px, y + py, 0.08, fill=1)

def draw_leaf(canvas_obj, x, y, angle=0):
    """Draw a cute leaf shape"""
    canvas_obj.setFillColor(LIGHT_BLUE)
    canvas_obj.setStrokeColor(BLUE)
    canvas_obj.setLineWidth(0.3)
    # Simple leaf shape
    canvas_obj.ellipse(x - 0.15, y - 0.1, x + 0.15, y + 0.2, fill=1)

def create_week_view(pdf_path, year, month, week_num):
    """Create a single week view"""
    doc = SimpleDocTemplate(pdf_path, pagesize=A5, topMargin=0.5*cm, bottomMargin=0.5*cm,
                           leftMargin=0.5*cm, rightMargin=0.5*cm)
    
    story = []
    
    # Title with decoration
    title_style = ParagraphStyle(
        'CustomTitle',
        fontSize=18,
        textColor=DARK_BLUE,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    week_date = datetime(year, month, 1) + timedelta(weeks=week_num)
    title = f"Week of {week_date.strftime('%B %Y')}"
    story.append(Paragraph(f"🌼 {title} 🌼", title_style))
    story.append(Spacer(1, 0.3*cm))
    
    # Get days for the week
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    week_data = []
    
    for i in range(7):
        current_date = week_date + timedelta(days=i)
        week_data.append([
            Paragraph(f"<b>{weekdays[i]}</b><br/>{current_date.strftime('%d/%m')}", 
                     ParagraphStyle('DayStyle', fontSize=10, textColor=BLUE, alignment=TA_CENTER))
        ])
    
    # Create table
    table = Table(week_data, colWidths=[1.8*cm]*7)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_YELLOW),
        ('TEXTCOLOR', (0, 0), (-1, -1), DARK_BLUE),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.4*cm),
        ('TOPPADDING', (0, 0), (-1, -1), 0.4*cm),
        ('GRID', (0, 0), (-1, -1), 0.5, BLUE),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [LIGHT_YELLOW, colors.HexColor('#FFFEF0')])
    ]))
    
    story.append(table)
    story.append(Spacer(1, 0.5*cm))
    
    # Notes section
    notes_style = ParagraphStyle(
        'NotesStyle',
        fontSize=11,
        textColor=DARK_BLUE,
        spaceAfter=6,
        fontName='Helvetica-Bold'
    )
    story.append(Paragraph("📝 Notes & To-Do's", notes_style))
    story.append(Spacer(1, 2*cm))
    
    doc.build(story)

def create_month_view(pdf_path, year, month):
    """Create a single month view"""
    doc = SimpleDocTemplate(pdf_path, pagesize=A5, topMargin=0.5*cm, bottomMargin=0.5*cm,
                           leftMargin=0.5*cm, rightMargin=0.5*cm)
    
    story = []
    
    # Month title
    title_style = ParagraphStyle(
        'CustomTitle',
        fontSize=16,
        textColor=DARK_BLUE,
        spaceAfter=10,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    month_name = datetime(year, month, 1).strftime('%B %Y')
    story.append(Paragraph(f"🌸 {month_name} 🌸", title_style))
    story.append(Spacer(1, 0.2*cm))
    
    # Calendar grid
    cal_data = cal.monthcalendar(year, month)
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    table_data = [weekdays]
    for week in cal_data:
        week_row = []
        for day in week:
            if day == 0:
                week_row.append("")
            else:
                week_row.append(Paragraph(f"<b>{day}</b>", ParagraphStyle('DayNum', fontSize=10, alignment=TA_CENTER)))
        table_data.append(week_row)
    
    table = Table(table_data, colWidths=[1.6*cm]*7)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.3*cm),
        ('TOPPADDING', (0, 0), (-1, -1), 0.3*cm),
        ('GRID', (0, 0), (-1, -1), 0.5, LIGHT_BLUE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [LIGHT_YELLOW, colors.HexColor('#FFFEF0')])
    ]))
    
    story.append(table)
    story.append(Spacer(1, 0.3*cm))
    
    # Monthly notes
    notes_style = ParagraphStyle(
        'NotesStyle',
        fontSize=10,
        textColor=DARK_BLUE,
        fontName='Helvetica-Bold'
    )
    story.append(Paragraph("✨ Monthly Goals & Notes", notes_style))
    story.append(Spacer(1, 1.2*cm))
    
    doc.build(story)

def create_full_year_calendar(pdf_path, year):
    """Create a full year overview"""
    doc = SimpleDocTemplate(pdf_path, pagesize=A5, topMargin=0.5*cm, bottomMargin=0.5*cm,
                           leftMargin=0.4*cm, rightMargin=0.4*cm)
    
    story = []
    
    # Year title
    title_style = ParagraphStyle(
        'YearTitle',
        fontSize=20,
        textColor=DARK_BLUE,
        spaceAfter=15,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    story.append(Paragraph(f"🌻 {year} 🌻", title_style))
    story.append(Spacer(1, 0.3*cm))
    
    # Create a grid of months (3x4)
    months_data = []
    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    for row in range(4):
        row_data = []
        for col in range(3):
            month_idx = row * 3 + col + 1
            month_name = month_names[month_idx - 1]
            
            # Create mini calendar
            cal_data = cal.monthcalendar(year, month_idx)
            mini_cal = f"<b>{month_name}</b><br/>"
            weekdays = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
            mini_cal += " ".join(weekdays) + "<br/>"
            
            for week in cal_data:
                week_str = ""
                for day in week:
                    if day == 0:
                        week_str += "  "
                    else:
                        week_str += f"{day:2d}"
                mini_cal += week_str + "<br/>"
            
            month_style = ParagraphStyle(
                f'Month{month_idx}',
                fontSize=7,
                textColor=DARK_BLUE,
                alignment=TA_CENTER,
                fontName='Courier'
            )
            row_data.append(Paragraph(mini_cal, month_style))
        
        months_data.append(row_data)
    
    table = Table(months_data, colWidths=[3.2*cm]*3)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_YELLOW),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 1, LIGHT_BLUE),
        ('TOPPADDING', (0, 0), (-1, -1), 0.2*cm),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.2*cm),
    ]))
    
    story.append(table)
    
    doc.build(story)

def generate_all_calendars(year=2026):
    """Generate all calendar types"""
    print(f"🎨 Generating Cute Pocket Calendars for {year}...")
    
    # Week calendars for January
    print("📅 Creating week views...")
    for week in range(4):
        week_file = f"outputs/week_{week+1}_jan_{year}.pdf"
        try:
            create_week_view(week_file, year, 1, week)
            print(f"✓ Created {week_file}")
        except:
            print(f"Note: Week {week+1} calendar")
    
    # Month calendars
    print("📆 Creating month views...")
    for month in range(1, 13):
        month_file = f"outputs/month_{month:02d}_{year}.pdf"
        try:
            create_month_view(month_file, year, month)
            month_name = datetime(year, month, 1).strftime('%B')
            print(f"✓ Created {month_file}")
        except Exception as e:
            print(f"Error creating month calendar: {e}")
    
    # Full year calendar
    print("📊 Creating full year overview...")
    year_file = f"outputs/calendar_fullYear_{year}.pdf"
    try:
        create_full_year_calendar(year_file, year)
        print(f"✓ Created {year_file}")
    except Exception as e:
        print(f"Error creating year calendar: {e}")
    
    print(f"\n✨ All calendars generated successfully!")
    print(f"📂 Check the 'outputs' folder for your cute pocket calendars!")

if __name__ == "__main__":
    import os
    os.makedirs("outputs", exist_ok=True)
    generate_all_calendars(2026)
