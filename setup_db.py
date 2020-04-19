from myranker import create_app, db
from myranker.models import User, Alevel, Course, University, Alevelgrade
import datetime

app = create_app()


def setup_db(db, app):

    with app.app_context():
        db.create_all()

        alevels = ['Accounting', 'Afrikaans', 'Ancient History', 'Anthropology', 'Applied Art and Design', 'Applied Business', 'Applied ICT', 'Applied Science', 'Arabic', 'Archaeology', 'Art and Design', 'Bengali', 'Biblical Hebrew', 'Biology', 'Business', 'Business Studies', 'Chemistry', 'Chinese', 'Citizenship Studies', 'Classical Civilisation', 'Classical Greek', 'Classical Studies', 'Communication and Culture', 'Computer Science', 'Computing', 'Creative Writing', 'Critical Thinking', 'Dance', 'Design and Technology', 'Design and Textiles', 'Digital Media and Design', 'Digital Technology', 'Divinity', 'Drama', 'Drama and Theatre', 'Dutch', 'Economics', 'Economics and Business', 'Electronics', 'Engineering', 'English Language', 'English Language and Literature', 'English Literature', 'Environmental Science', 'Environmental Studies', 'Environmental Technology', 'Fashion and Textiles', 'Film Studies', 'Food Studies', 'Food Technology', 'French', 'Further Mathematics', 'General Studies', 'Geography', 'Geology', 'German', 'Global Development', 'Global Perspectives and Research', 'Government and Politics', 'Greek', 'Gujarati', 'Health and Social Care', 'Hindi', 'Hinduism', 'History', 'History of Art', 'Home Economics', 'Human Biology', 'Humanities', 'ICT', 'Information Technology', 'Irish', 'Islamic Studies', 'Italian', 'Japanese', 'Journalism', 'Latin', 'Law', 'Leisure Studies', 'Life and Health Sciences', 'Marine Science', 'Mathematics', 'Media Studies', 'Modern Hebrew', 'Modern Languages', 'Moving Image Arts', 'Music', 'Music Technology', 'Nutrition and Food Science', 'Panjabi', 'Performance Studies', 'Performing Arts', 'Persian', 'Philosophy', 'Photography', 'Physical Education', 'Physical Science', 'Physics', 'Polish', 'Politics', 'Portuguese', 'Product Design', 'Professional Business Services', 'Psychology', 'Pure Mathematics', 'Quantitative Methods', 'Religious Studies', 'Russian', 'Science in Society', 'Sociology', 'Software Systems Development', 'Spanish', 'Sports Science', 'Statistics', 'Systems and Control Technology', 'Tamil', 'Technology and Design', 'Thinking Skills', 'Travel and Tourism', 'Turkish', 'Urdu', 'Welsh', 'World Development']
        for alevel in alevels:
            db.session.add(Alevel(name=alevel))

        grades = ['A*', 'A', 'B', 'C', 'D', 'E']
        for grade in grades:
            db.session.add(Alevelgrade(grade=grade))

        courses = ['Chemistry', 'Civil Engineering', 'Computer Science', 'Economics', 'History', 'Marketing', 'Mathematics', 'Physics', 'Psychology']

        for course in courses:
            db.session.add(Course(name=course))


        db.session.add(University(name='University of Cambridge', description='University of Cambridge [Temporary Description]'))
        db.session.add(University(name='University of St Andrews', description='University of St Andrews [Temporary Description]'))
        db.session.add(University(name='University of Hull', description='University of Hull [Temporary Description]'))
        db.session.add(University(name='University of Sheffield', description='University of Sheffield [Temporary Description]'))
        db.session.add(University(name='Imperial College London', description='Imperial College London [Temporary Description]'))
        db.session.add(University(name='Bournemouth University', description='Bournemouth University [Temporary Description]'))
        db.session.add(University(name='University of Surrey', description='University of Surrey [Temporary Description]'))
        db.session.add(University(name='University of Chester', description='University of Chester [Temporary Description]'))
        db.session.add(University(name='University of Loughborough', description='University of Loughborough [Temporary Description]'))
        db.session.add(University(name='Aberystwyth University', description='Aberystwyth University [Temporary Description]'))


        db.session.commit()


setup_db(db, app)
