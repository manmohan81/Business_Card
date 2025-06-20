# Professional Business Card - Streamlit App

A beautiful, interactive professional business card application built with Streamlit for **Manmohan Singh Rawat**, Senior Design & Development Engineer.

## Features

- 🎨 **Beautiful Design**: Modern, professional layout with gradient backgrounds
- 📱 **Responsive**: Works perfectly on desktop and mobile devices
- 🔄 **Interactive**: Clickable contact buttons and social links
- 📥 **vCard Download**: Download contact information as a .vcf file
- ⚡ **Fast Loading**: Optimized Streamlit application

## Business Information

- **Name**: Manmohan Singh Rawat
- **Title**: Senior Design & Development Engineer
- **Qualification**: B.E Mechanical Engineering
- **Experience**: 22 Years in Design & Development
- **Specialties**: Mechanical Design, Product Development, CAD/CAM Systems, Project Management

## Installation & Usage

### Option 1: Run Locally

1. **Install Python** (3.8 or higher)
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   streamlit run streamlit_app.py
   ```
4. **Open your browser** to `http://localhost:8501`

### Option 2: Deploy to Streamlit Cloud

1. **Upload to GitHub**: Create a repository with these files
2. **Visit**: [share.streamlit.io](https://share.streamlit.io)
3. **Deploy**: Connect your GitHub repository
4. **Share**: Get a public URL to share your business card

### Option 3: Deploy to Other Platforms

- **Heroku**: Add a `Procfile` with `web: streamlit run streamlit_app.py --server.port=$PORT`
- **Railway**: Direct deployment from GitHub
- **Render**: Connect repository and deploy

## File Structure

```
├── streamlit_app.py      # Main application file
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Customization

To customize for your own use:

1. **Edit business information** in the `business_info` dictionary
2. **Modify colors** in the CSS section
3. **Add/remove sections** as needed
4. **Update contact information** and social links

## Features Included

- ✅ Professional card layout
- ✅ Contact information display
- ✅ Experience and qualifications
- ✅ Core specialties showcase
- ✅ Certifications list
- ✅ Social media links
- ✅ Interactive contact buttons
- ✅ vCard download functionality
- ✅ Mobile-responsive design
- ✅ Modern gradient styling

## Technologies Used

- **Streamlit**: Web application framework
- **HTML/CSS**: Custom styling
- **Python**: Backend logic

## License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Streamlit**