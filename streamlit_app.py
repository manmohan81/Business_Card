import streamlit as st
import base64
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Manmohan Singh Rawat - Professional Business Card",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1e3a8a;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .sub-header {
        text-align: center;
        color: #64748b;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .business-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        border: 1px solid #e2e8f0;
        margin: 2rem 0;
    }
    
    .card-header {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    
    .profile-icon {
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 1.5rem;
        font-size: 2rem;
        color: white;
    }
    
    .name-title {
        flex: 1;
    }
    
    .name {
        font-size: 2rem;
        font-weight: bold;
        color: #1f2937;
        margin: 0;
    }
    
    .title {
        font-size: 1.2rem;
        color: #2563eb;
        font-weight: 600;
        margin: 0.25rem 0;
    }
    
    .company {
        color: #6b7280;
        font-size: 1rem;
    }
    
    .qualification {
        color: #059669;
        font-size: 0.9rem;
        margin-top: 0.5rem;
        display: flex;
        align-items: center;
    }
    
    .contact-info {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .contact-item {
        display: flex;
        align-items: center;
        padding: 0.75rem;
        background: #f8fafc;
        border-radius: 10px;
    }
    
    .contact-icon {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 1rem;
        font-size: 1.2rem;
    }
    
    .email-icon { background: #dbeafe; color: #2563eb; }
    .phone-icon { background: #dcfce7; color: #16a34a; }
    .location-icon { background: #fecaca; color: #dc2626; }
    .experience-icon { background: #fef3c7; color: #d97706; }
    
    .professional-details {
        background: linear-gradient(135deg, #ea580c 0%, #dc2626 100%);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
    }
    
    .details-header {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    
    .details-icon {
        font-size: 2rem;
        margin-right: 1rem;
        color: #fbbf24;
    }
    
    .specialties-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.5rem;
        margin: 1rem 0;
    }
    
    .specialty-item {
        background: rgba(255, 255, 255, 0.2);
        padding: 0.5rem 1rem;
        border-radius: 10px;
        font-size: 0.9rem;
    }
    
    .certification-item {
        display: flex;
        align-items: center;
        margin: 0.5rem 0;
    }
    
    .cert-bullet {
        width: 8px;
        height: 8px;
        background: #fbbf24;
        border-radius: 50%;
        margin-right: 0.75rem;
    }
    
    .info-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 3rem 0;
    }
    
    .info-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        color: white;
    }
    
    .card-icon {
        width: 50px;
        height: 50px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
        font-size: 1.5rem;
        color: white;
    }
    
    .orange-bg { background: #ea580c; }
    .blue-bg { background: #2563eb; }
    .green-bg { background: #16a34a; }
    
    .card-title {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .card-description {
        font-size: 0.9rem;
        color: #cbd5e1;
        line-height: 1.5;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #4338ca 100%);
    }
    
    .social-links {
        display: flex;
        gap: 1rem;
        margin-top: 1.5rem;
    }
    
    .social-link {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-decoration: none;
        font-size: 1.2rem;
        transition: all 0.3s ease;
    }
    
    .linkedin-bg { background: #0077b5; }
    .website-bg { background: #6b7280; }
    
    .social-link:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Business information
    business_info = {
        "name": "MANMOHAN SINGH RAWAT",
        "title": "Mechanical Design Manager",
        "company": "Engineering Solutions Ltd.",
        "email": "manmohan.rawat@gmail.com",
        "phone": "+91 9916225795",
        "location": "New Delhi, India",
        "linkedin": "linkedin.com/in/manmohanrawat",
        "website": "https://incomparable-unicorn-cb5a02.netlify.app",
        "qualification": "B.E Mechanical Engineering",
        "experience": "22 Years Experience",
        "field": "Design & Development",
        "specialties": ["Mechanical Design", "Product Development", "CAD/CAM Systems", "Project Management"],
        "certifications": ["B.E Mechanical Engineering", "PMP Certified", "AutoCAD Professional", "SolidWorks Expert"]
    }
    
    # Header
    st.markdown('<h1 class="main-header">Professional Business Card</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Engineering Excellence in Design & Development</p>', unsafe_allow_html=True)
    
    # Main business card
    st.markdown(f"""
    <div class="business-card">
        <div class="card-header">
            <div class="profile-icon">👨‍💼</div>
            <div class="name-title">
                <h2 class="name">{business_info['name']}</h2>
                <p class="title">{business_info['title']}</p>
                <p class="company">{business_info['company']}</p>
                <p class="qualification">🎓 {business_info['qualification']}</p>
            </div>
            <div style="font-size: 3rem; color: #ea580c;">⚙️</div>
        </div>
        
        <div class="contact-info">
            <div class="contact-item">
                <div class="contact-icon email-icon">📧</div>
                <span>{business_info['email']}</span>
            </div>
            <div class="contact-item">
                <div class="contact-icon phone-icon">📱</div>
                <span>{business_info['phone']}</span>
            </div>
            <div class="contact-item">
                <div class="contact-icon location-icon">📍</div>
                <span>{business_info['location']}</span>
            </div>
            <div class="contact-item">
                <div class="contact-icon experience-icon">📅</div>
                <span>{business_info['experience']} • {business_info['field']}</span>
            </div>
        </div>
        
        <div class="social-links">
            <a href="https://{business_info['linkedin']}" class="social-link linkedin-bg" target="_blank">💼</a>
            <a href="https://{business_info['website']}" class="social-link website-bg" target="_blank">🌐</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Professional details section
    st.markdown(f"""
    <div class="professional-details">
        <div class="details-header">
            <span class="details-icon">⚙️</span>
            <h3 style="margin: 0; font-size: 1.5rem;">Engineering Excellence</h3>
        </div>
        
        <div style="margin-bottom: 1.5rem;">
            <h4 style="color: #fed7aa; margin-bottom: 0.75rem;">Core Specialties:</h4>
            <div class="specialties-grid">
                {"".join([f'<div class="specialty-item">{specialty}</div>' for specialty in business_info['specialties']])}
            </div>
        </div>
        
        <div>
            <h4 style="color: #fed7aa; margin-bottom: 0.75rem;">Qualifications & Certifications:</h4>
            {"".join([f'<div class="certification-item"><div class="cert-bullet"></div><span style="font-size: 0.9rem;">{cert}</span></div>' for cert in business_info['certifications']])}
        </div>
        
        <div style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.2);">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <span>💼 {business_info['linkedin']}</span>
            </div>
            <div style="display: flex; align-items: center; gap: 1rem; margin-top: 0.5rem;">
                <span>🌐 {business_info['website']}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Information cards
    st.markdown("""
    <div class="info-cards">
        <div class="info-card">
            <div class="card-icon orange-bg">⚙️</div>
            <h3 class="card-title">Mechanical Design</h3>
            <p class="card-description">Expert in mechanical system design with 22 years of hands-on engineering experience.</p>
        </div>
        
        <div class="info-card">
            <div class="card-icon blue-bg">💼</div>
            <h3 class="card-title">Product Development</h3>
            <p class="card-description">Comprehensive product development from concept to manufacturing with proven track record.</p>
        </div>
        
        <div class="info-card">
            <div class="card-icon green-bg">🎓</div>
            <h3 class="card-title">Technical Excellence</h3>
            <p class="card-description">B.E Mechanical Engineering foundation with advanced CAD/CAM and project management expertise.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive features
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📧 Contact via Email", use_container_width=True):
            st.success(f"Email: {business_info['email']}")
    
    with col2:
        if st.button("📱 Call Now", use_container_width=True):
            st.success(f"Phone: {business_info['phone']}")
    
    with col3:
        if st.button("💼 View LinkedIn", use_container_width=True):
            st.success(f"LinkedIn: {business_info['linkedin']}")
    
    # Download vCard feature
    st.markdown("---")
    st.subheader("📱 Digital Business Card")
    
    # Create vCard content
    vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{business_info['name']}
ORG:{business_info['company']}
TITLE:{business_info['title']}
EMAIL:{business_info['email']}
TEL:{business_info['phone']}
ADR:;;{business_info['location']};;;;
URL:https://{business_info['website']}
NOTE:Qualification: {business_info['qualification']}\\nExperience: {business_info['experience']}\\nField: {business_info['field']}\\nSpecialties: {', '.join(business_info['specialties'])}
END:VCARD"""
    
    st.download_button(
        label="📥 Download vCard (.vcf)",
        data=vcard_content,
        file_name=f"{business_info['name'].replace(' ', '_')}_business_card.vcf",
        mime="text/vcard",
        use_container_width=True
    )
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #cbd5e1; padding: 2rem;'>"
        f"<p>© 2025 {business_info['name']} | Professional Business Card</p>"
        "<p>Built with Streamlit 🚀</p>"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
