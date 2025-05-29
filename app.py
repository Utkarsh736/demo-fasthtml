from fasthtml.common import *

# Custom CSS for modern design
css = Style("""
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        line-height: 1.6;
        color: #333;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 2rem;
    }
    
    header {
        padding: 2rem 0;
        text-align: center;
        color: white;
    }
    
    .hero {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 4rem 2rem;
        margin: 2rem 0;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .hero h1 {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #fff, #f0f0f0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero p {
        font-size: 1.3rem;
        opacity: 0.9;
        max-width: 600px;
        margin: 0 auto;
    }
    
    .section {
        background: white;
        margin: 2rem 0;
        border-radius: 15px;
        padding: 3rem 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .section:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    
    .section h2 {
        color: #2c3e50;
        margin-bottom: 2rem;
        font-size: 2.5rem;
        text-align: center;
        position: relative;
    }
    
    .section h2:after {
        content: '';
        display: block;
        width: 50px;
        height: 3px;
        background: linear-gradient(45deg, #667eea, #764ba2);
        margin: 1rem auto;
        border-radius: 2px;
    }
    
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .skill-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .skill-card:hover {
        transform: scale(1.05);
    }
    
    .skill-card h3 {
        margin-bottom: 1rem;
        font-size: 1.3rem;
    }
    
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .project-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 2rem;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        background: #e9ecef;
        transform: translateX(10px);
    }
    
    .project-card h3 {
        color: #2c3e50;
        margin-bottom: 1rem;
        font-size: 1.4rem;
    }
    
    .project-card p {
        color: #666;
        margin-bottom: 1rem;
    }
    
    .tech-tag {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        margin: 0.2rem;
    }
    
    .contact-form {
        max-width: 600px;
        margin: 0 auto;
    }
    
    .form-group {
        margin-bottom: 1.5rem;
    }
    
    .form-group label {
        display: block;
        margin-bottom: 0.5rem;
        color: #2c3e50;
        font-weight: 500;
    }
    
    .form-group input,
    .form-group textarea {
        width: 100%;
        padding: 1rem;
        border: 2px solid #e9ecef;
        border-radius: 8px;
        font-size: 1rem;
        transition: border-color 0.3s ease;
    }
    
    .form-group input:focus,
    .form-group textarea:focus {
        outline: none;
        border-color: #667eea;
    }
    
    .btn {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 8px;
        font-size: 1.1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        display: block;
        margin: 0 auto;
    }
    
    .btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
    }
    
    .social-links {
        text-align: center;
        margin-top: 2rem;
    }
    
    .social-links a {
        display: inline-block;
        margin: 0 1rem;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border-radius: 50%;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    .social-links a:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-3px);
    }
    
    footer {
        text-align: center;
        padding: 2rem;
        color: white;
        opacity: 0.8;
    }
    
    @media (max-width: 768px) {
        .hero h1 {
            font-size: 2.5rem;
        }
        
        .container {
            padding: 0 1rem;
        }
        
        .section {
            padding: 2rem 1rem;
        }
    }
    
    .fade-in {
        animation: fadeIn 0.8s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
""")

# JavaScript for smooth scrolling and animations
js = Script("""
    document.addEventListener('DOMContentLoaded', function() {
        // Add fade-in animation to sections
        const sections = document.querySelectorAll('.section');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in');
                }
            });
        }, { threshold: 0.1 });
        
        sections.forEach(section => {
            observer.observe(section);
        });
        
        // Form submission handler
        const form = document.getElementById('contact-form');
        if (form) {
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                alert('Thank you for your message! This is a demo - no actual email was sent.');
                form.reset();
            });
        }
    });
""")

app = FastHTML(hdrs=[css, js])

@app.get("/")
def home():
    return Html(
        Head(
            Title("Alex Johnson - Full Stack Developer"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Link(href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap", rel="stylesheet")
        ),
        Body(
            # Header
            Header(
                Div(
                    H1("Portfolio", style="font-size: 2rem; font-weight: 300; letter-spacing: 2px;"),
                    cls="container"
                )
            ),
            
            # Hero Section
            Div(
                Div(
                    H1("Alex Johnson"),
                    P("Full Stack Developer & UI/UX Enthusiast"),
                    P("Crafting digital experiences with modern web technologies", 
                      style="margin-top: 1rem; font-size: 1.1rem; opacity: 0.8;"),
                    cls="hero"
                ),
                cls="container"
            ),
            
            # About Section
            Div(
                Div(
                    H2("About Me"),
                    P("I'm a passionate full-stack developer with 5+ years of experience building scalable web applications. I love creating intuitive user interfaces and robust backend systems that solve real-world problems.", 
                      style="font-size: 1.2rem; text-align: center; max-width: 800px; margin: 0 auto; color: #666;"),
                    P("When I'm not coding, you can find me exploring new technologies, contributing to open-source projects, or hiking in the mountains.",
                      style="font-size: 1.2rem; text-align: center; max-width: 800px; margin: 2rem auto 0; color: #666;"),
                    cls="section"
                ),
                cls="container"
            ),
            
            # Skills Section
            Div(
                Div(
                    H2("Skills & Technologies"),
                    Div(
                        Div(
                            H3("Frontend"),
                            P("React, Vue.js, TypeScript, Tailwind CSS, Next.js"),
                            cls="skill-card"
                        ),
                        Div(
                            H3("Backend"),
                            P("Python, Node.js, FastAPI, Django, PostgreSQL"),
                            cls="skill-card"
                        ),
                        Div(
                            H3("DevOps & Cloud"),
                            P("Docker, AWS, GitHub Actions, Nginx"),
                            cls="skill-card"
                        ),
                        Div(
                            H3("Tools & Others"),
                            P("Git, Figma, REST APIs, GraphQL, Testing"),
                            cls="skill-card"
                        ),
                        cls="skills-grid"
                    ),
                    cls="section"
                ),
                cls="container"
            ),
            
            # Projects Section
            Div(
                Div(
                    H2("Featured Projects"),
                    Div(
                        Div(
                            H3("E-Commerce Platform"),
                            P("A full-stack e-commerce solution with real-time inventory management, payment processing, and admin dashboard."),
                            Div(
                                Span("React", cls="tech-tag"),
                                Span("Node.js", cls="tech-tag"),
                                Span("MongoDB", cls="tech-tag"),
                                Span("Stripe", cls="tech-tag"),
                            ),
                            cls="project-card"
                        ),
                        Div(
                            H3("Task Management App"),
                            P("A collaborative project management tool with real-time updates, file sharing, and team communication features."),
                            Div(
                                Span("Vue.js", cls="tech-tag"),
                                Span("FastAPI", cls="tech-tag"),
                                Span("PostgreSQL", cls="tech-tag"),
                                Span("WebSocket", cls="tech-tag"),
                            ),
                            cls="project-card"
                        ),
                        Div(
                            H3("Analytics Dashboard"),
                            P("A comprehensive analytics platform with interactive charts, real-time data processing, and custom reporting."),
                            Div(
                                Span("React", cls="tech-tag"),
                                Span("D3.js", cls="tech-tag"),
                                Span("Python", cls="tech-tag"),
                                Span("Redis", cls="tech-tag"),
                            ),
                            cls="project-card"
                        ),
                        cls="projects-grid"
                    ),
                    cls="section"
                ),
                cls="container"
            ),
            
            # Contact Section
            Div(
                Div(
                    H2("Get In Touch"),
                    P("I'm always interested in new opportunities and exciting projects. Let's connect!",
                      style="text-align: center; font-size: 1.2rem; color: #666; margin-bottom: 2rem;"),
                    Form(
                        Div(
                            Label("Name", For="name"),
                            Input(type="text", id="name", name="name", required=True),
                            cls="form-group"
                        ),
                        Div(
                            Label("Email", For="email"),
                            Input(type="email", id="email", name="email", required=True),
                            cls="form-group"
                        ),
                        Div(
                            Label("Message", For="message"),
                            Textarea(id="message", name="message", rows="5", placeholder="Tell me about your project...", required=True),
                            cls="form-group"
                        ),
                        Button("Send Message", type="submit", cls="btn"),
                        id="contact-form",
                        cls="contact-form"
                    ),
                    Div(
                        A("LinkedIn", href="#", style="text-decoration: none;"),
                        A("GitHub", href="#", style="text-decoration: none;"),
                        A("Twitter", href="#", style="text-decoration: none;"),
                        A("Email", href="#", style="text-decoration: none;"),
                        cls="social-links"
                    ),
                    cls="section"
                ),
                cls="container"
            ),
            
            # Footer
            Footer(
                P("© 2025 Alex Johnson. Built with FastHTML ⚡", 
                  style="margin: 0;"),
                P("Crafted with passion and modern web technologies",
                  style="margin: 0.5rem 0 0 0; opacity: 0.7; font-size: 0.9rem;")
            )
        )
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
