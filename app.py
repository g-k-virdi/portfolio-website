from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Portfolio data based on Gurleen's resume and wireframe
portfolio_data = {
    'name': 'Gurleen Kaur Virdi',
    'title': 'Industrial Engineering Student',
    'about': 'I am an Industrial Engineering student with a passion for building human-centered designs. I strongly believe that designing isn\'t just about aesthetics, it\'s about creating intuitive systems that reduce cognitive load and eliminate friction.',
    'quote': 'A product is only as good as it can be used',
    'skills': [
        {'category': 'UX & Human Factors', 'skill_list': [
            {'name': 'Human Factors Engineering', 'icon': 'fas fa-users-cog'},
            {'name': 'Wireframing', 'icon': 'fas fa-pencil-ruler'},
            {'name': 'Usability Testing', 'icon': 'fas fa-user-check'},
            {'name': 'Prototyping', 'icon': 'fas fa-layer-group'},
            {'name': 'User Interface Design', 'icon': 'fas fa-desktop'}
        ]},
        {'category': 'Data & Analysis', 'skill_list': [
            {'name': 'Data Analysis', 'icon': 'fas fa-chart-line'},
            {'name': 'Data Visualization', 'icon': 'fas fa-chart-bar'},
            {'name': 'Exploratory Data Analysis', 'icon': 'fas fa-search'},
            {'name': 'Time Series Analysis', 'icon': 'fas fa-chart-area'},
            {'name': 'Process Modeling', 'icon': 'fas fa-project-diagram'},
            {'name': 'Optimization', 'icon': 'fas fa-sliders-h'}
        ]},
        {'category': 'Programming & Tools', 'skill_list': [
            {'name': 'Python', 'icon': 'fab fa-python'},
            {'name': 'Java', 'icon': 'fab fa-java'},
            {'name': 'SQL', 'icon': 'fas fa-database'},
            {'name': 'Pandas', 'icon': 'fas fa-table'},
            {'name': 'Tableau', 'icon': 'fas fa-chart-pie'}
        ]},
        {'category': 'Soft Skills', 'skill_list': [
            {'name': 'Teamwork', 'icon': 'fas fa-users'},
            {'name': 'Project Management', 'icon': 'fas fa-tasks'},
            {'name': 'Customer Service', 'icon': 'fas fa-concierge-bell'},
            {'name': 'Communication', 'icon': 'fas fa-comments'},
            {'name': 'Problem Solving', 'icon': 'fas fa-brain'}
        ]}
    ],
    'projects': [
        {
            'title': 'Kritik Activity Creation Module Redesign',
            'description': 'Employed cognitive walkthroughs and heuristic evaluations to identify design issues in the activity module of Kritik. Developed low-fidelity prototypes and conducted usability testing and task analysis on them in a team of three students.'
        },
        {
            'title': 'Electric Vehicle Recommendation System Design',
            'description': 'Designed a user-centric web application to recommend electric vehicles using Java Spring Boot backend and React.js frontend in a team of three industrial engineering students.'
        },
        {
            'title': 'Pollution Forecasting Using Time-Series Analysis',
            'description': 'Developed time-series forecasting models using Holt-Winters and SARIMA methods to predict pollution levels. Analyzed seasonal trends, patterns, and historical patterns to improve forecast accuracy.'
        },
        {
            'title': 'NHL Draft Prediction Using Machine Learning',
            'description': 'Built classification and regression models to predict NHL standings and simulate draft outcomes using 10 years of data. Cleaned and engineered features to improve model accuracy and performance.'
        }
    ],
    'contact': {
        'email': 'virdigurleenkaur3@gmail.com',
        'linkedin': 'https://www.linkedin.com/in/gurleen-kaur-virdi-a918a12ab/',
        'location': 'Toronto, Ontario, Canada'
    },
    'education': {
        'degree': 'Bachelor of Applied Science - Industrial Engineering',
        'institution': 'University of Toronto',
        'location': 'Toronto, Ontario, Canada',
        'period': 'September 2022 -- June 2026',
        'coursework': 'Human Factors Engineering, Foundations of Cognitive Psychology, Design & Analysis of Information Systems, Data Modelling, Organizational Design, Engineering Strategies & Practice, Engineering Economics'
    },
    'experience': [
        {
            'position': 'Data Analytics Intern',
            'company': 'Data Joins',
            'location': 'Remote',
            'period': 'June 2025 – Present',
            'description': 'Perform data cleaning, exploratory data analysis (EDA), and predictive modeling on datasets like purchase and export dataset. Develop interactive dashboards to visualize key performance indicators and enable data-driven decision-making.'
        },
        {
            'position': 'Team Member',
            'company': 'RaPizza',
            'location': 'Brampton, Ontario, Canada',
            'period': 'May 2022 – September 2024',
            'description': 'Worked collaboratively to prepare and serve meals, ensuring smooth operations and good customer service.'
        },
        {
            'position': 'Volunteer',
            'company': 'Rexdale Women\'s Center',
            'location': 'Etobicoke, Ontario, Canada',
            'period': 'July 2019 – September 2019',
            'description': 'Worked under supervision to assist new immigrants in person and on call. Filled legal forms, analyzed and updated files, and established healthy client relationships.'
        }
    ],
    'extracurriculars': [
        {
            'position': 'Financial Director',
            'company': 'University of Toronto Autism Alliance (UTAA)',
            'location': 'Toronto, Ontario, Canada',
            'period': 'September 2023 – Present',
            'description': 'Oversee accounting operations, manage budgets, and ensure financial efficiency for the club. Collaborate with team members to plan and organize events for individuals on the autism spectrum.'
        },
        {
            'position': 'Peer Mentor',
            'company': 'University of Toronto Indy Club',
            'location': 'Toronto, Ontario, Canada',
            'period': 'September 2023 – May 2024',
            'description': 'Provided academic and personal support to a first-year engineering student.'
        },
        {
            'position': 'Digital Content Creator',
            'company': 'Freelance',
            'location': 'Toronto, Ontario, Canada',
            'period': 'April 2023 – July 2024',
            'description': 'Produced and translated poetry content paired with visual storytelling. Grew audience to 15K+ followers in four months across a digital platform.'
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    # Here you would typically send an email or save to database
    # For now, we'll just return a success message
    return jsonify({'message': 'Thank you for your message! I\'ll get back to you soon.'})

@app.route('/api/projects')
def get_projects():
    return jsonify(portfolio_data['projects'])

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=4000) 