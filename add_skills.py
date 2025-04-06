#!/usr/bin/env python
"""
Script to add skills to the database.
Usage: 
    python manage.py shell < add_skills.py
"""
from skills.models import Skill

# Define the skills data
skills_data = [
    {
        "title": "Django",
        "category": "track1",
        "order": 0,
        "description": "Building robust web applications with REST APIs, authentication systems, and database modeling. Experienced in creating scalable Django projects with best practices.",
        "icon": "fab fa-python"  # Using Python icon since there's no specific Django icon in FA
    },
    {
        "title": "Golang",
        "category": "track1",
        "order": 0,
        "description": "Developing high-performance microservices and backend systems using Go. Proficient with concurrency patterns and efficient memory management for optimal performance.",
        "icon": "fas fa-code"
    },
    {
        "title": "Git & GitHub",
        "category": "track1",
        "order": 0,
        "description": "Advanced skills in version control, branching strategies, and CI/CD integration. Experienced in managing repositories and collaborating with distributed teams.",
        "icon": "fab fa-github"
    },
    {
        "title": "C++",
        "category": "track1",
        "order": 0,
        "description": "Strong knowledge of C++ including memory management, STL, and multithreading. Experienced in performance optimization for competitive programming and application development.",
        "icon": "fas fa-file-code"
    },
    {
        "title": "Python",
        "category": "track1",
        "order": 1,
        "description": "Expert-level Python programming for web development, data analysis, and automation. Proficient with popular libraries including Django, Flask, Pandas, and NumPy.",
        "icon": "fab fa-python"
    },
    {
        "title": "Problem Solving",
        "category": "track1",
        "order": 3,
        "description": "Exceptional ability to analyze complex challenges and develop efficient solutions. Skilled in algorithmic thinking and optimization techniques for diverse technical problems.",
        "icon": "fas fa-lightbulb"
    },
    {
        "title": "Testing",
        "category": "track1",
        "order": 4,
        "description": "Comprehensive experience with unit, integration, and end-to-end testing methodologies. Proficient with testing frameworks like pytest, Jest, and Selenium for quality assurance.",
        "icon": "fas fa-vial"
    },
    {
        "title": "Leadership",
        "category": "track2",
        "order": 0,
        "description": "Leading technical teams, facilitating agile processes, and driving projects to completion. Experienced in mentoring junior developers and fostering collaborative work environments.",
        "icon": "fas fa-users"
    },
    {
        "title": "Linux",
        "category": "track2",
        "order": 0,
        "description": "Advanced Linux systems administration, bash scripting, and service configuration. Experienced with Ubuntu, CentOS, and Debian for development and production environments.",
        "icon": "fab fa-linux"
    },
    {
        "title": "Relational Databases",
        "category": "track2",
        "order": 0,
        "description": "Extensive knowledge of database design, normalization, and optimization techniques. Proficient with PostgreSQL, MySQL, and SQLite for application development and data management.",
        "icon": "fas fa-database"
    },
    {
        "title": "SQL",
        "category": "track2",
        "order": 0,
        "description": "Expert-level SQL proficiency with complex queries and performance optimization. Skilled in stored procedures and transaction management across various database systems.",
        "icon": "fas fa-table"
    },
    {
        "title": "Competitive Programming",
        "category": "track2",
        "order": 0,
        "description": "Active participant in programming competitions with strong algorithmic skills. Proficient in data structures, dynamic programming, and graph theory for solving complex problems efficiently.",
        "icon": "fas fa-trophy"
    },
    {
        "title": "Debugging",
        "category": "track2",
        "order": 0,
        "description": "Advanced debugging across multiple languages and environments. Skilled in identifying root causes of issues and implementing effective solutions for complex software problems.",
        "icon": "fas fa-bug"
    },
    {
        "title": "Teaching & Mentoring",
        "category": "track2",
        "order": 2,
        "description": "Passionate educator with experience developing technical curriculum and workshops. Effective at breaking down complex concepts and mentoring junior developers in their career path.",
        "icon": "fas fa-chalkboard-teacher"
    },
]

# Clear existing skills (optional, remove this if you want to keep existing skills)
print("Clearing existing skills...")
Skill.objects.all().delete()

# Add skills
print("Adding skills...")
for skill_data in skills_data:
    skill = Skill.objects.create(**skill_data)
    print(f"Added skill: {skill.title} ({skill.category})")

print("\nSkills summary:")
for category in ["track1", "track2"]:
    count = Skill.objects.filter(category=category).count()
    print(f"{category}: {count} skills")

print(f"Total: {Skill.objects.count()} skills added")
print("Done!") 