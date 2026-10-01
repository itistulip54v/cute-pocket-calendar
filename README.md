# 🌻 Cute Pocket Calendar Generator

A beautiful, pocket-friendly (A5 size) calendar generator with cute hand-drawn textures, floral patterns, and a charming blue and yellow color scheme!

## ✨ Features

- **Pocket-Friendly A5 Size**: Perfect for small notebooks and planners
- **Multiple View Options**:
  - 📅 **Week View**: Detailed weekly layouts with notes section
  - 📆 **Month View**: Calendar grid with monthly goals area
  - 📊 **Full Year View**: Compact 12-month overview
- **Cute Design Elements**:
  - 🌼 Hand-drawn style flowers and petals
  - 🎨 Decorative dot patterns
  - 🌿 Leafy embellishments
  - Soft textures throughout
- **Color Scheme**:
  - Primary Blue: #4A90E2
  - Accent Yellow: #FFD700
  - Light pastels for modern look
- **Easy to Customize**: Modify colors, fonts, and decorations in the code

## 📋 Requirements

- Python 3.7+
- reportlab
- matplotlib
- Pillow

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/itistulip54v/cute-pocket-calendar.git
cd cute-pocket-calendar
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the calendar generator:
```bash
python generate_calendar.py
```

This will create an `outputs/` folder with all your calendars:
- `week_1_jan_2026.pdf` through `week_4_jan_2026.pdf` - Week views
- `month_01_2026.pdf` through `month_12_2026.pdf` - Month views
- `calendar_fullYear_2026.pdf` - Full year overview

## 🎨 Customization

Edit `generate_calendar.py` to customize:

### Change Colors
```python
BLUE = colors.HexColor('#YOUR_COLOR_HEX')
YELLOW = colors.HexColor('#YOUR_COLOR_HEX')
```

### Change Year
```python
generate_all_calendars(2027)  # For year 2027
```

### Add More Decorative Elements
Modify the `draw_decorative_flowers()` and `draw_decorative_dots()` functions to add your own patterns!

## 📐 Calendar Details

### Week View
- Shows 7 days with dates
- Large space for daily notes and to-do's
- Perfect for detailed planning

### Month View
- Traditional calendar grid
- All dates visible at once
- Space for monthly goals and notes

### Full Year View
- All 12 months on one page
- Compact mini calendars
- Great for quick reference

## 📦 Output Format

All calendars are generated as PDF files with:
- A5 page size (148 × 210 mm / 5.8" × 8.3")
- Professional formatting
- Print-ready quality
- Cute, cohesive design

## 🌟 Tips for Best Results

1. **Printing**: Use quality paper (80-100 gsm) for best results
2. **Color**: Print in color to see the beautiful blue and yellow palette
3. **Binding**: A5 size is perfect for binding or using in pocket-sized planners
4. **Personalization**: Print multiple copies and customize each one by hand!

## 🎯 Use Cases

- 📓 Personal planners
- 🎓 Student organizers
- 💼 Desk accessories
- 🎁 Thoughtful gifts
- 📱 Digital or printed viewing

## 📝 License

This project is open source and available for personal and commercial use.

## 🤝 Contributing

Feel free to fork this repository and add your own enhancements!

### Ideas for Contributions:
- Add more decorative patterns
- Create different color schemes
- Add holiday markers
- Create habit tracking sections
- Add weekly themes

---

Made with 💙💛 for organized and cute planning! 🌸
