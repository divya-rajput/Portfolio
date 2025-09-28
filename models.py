from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Text


# class PersonalInformation(Base):
#     __tablename__ = 'personalinformation'

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     designation = Column(String)
#     description = Column(String)
#     phone_number = Column(String)
#     github_link = Column(String, unique=True)
#     linkedin_link = Column(String, unique=True)


# class Experience(Base):
#     __tablename__ = 'experience'

#     id = Column(Integer, primary_key=True, index=True)
#     company_name = Column(String)
#     role = Column(String)
#     start_date = Column(Date)
#     end_date = Column(Date)

#     projects = relationship("Project", back_populates="experience")


# class Project(Base):
#     __tablename__ = 'project'

#     id = Column(Integer, primary_key=True, index=True)
#     project_name = Column(String)
#     experience_id = Column(Integer, ForeignKey("experience.id"))
#     tag = Column(String)
#     experience = relationship("Experience", back_populates="projects")
#     descriptions = relationship("ProjectDescription", back_populates="project")


# class ProjectDescription(Base):
#     __tablename__ = 'project_description'
#     id = Column(Integer, primary_key=True, index=True)
#     description = Column(Text)
#     project_id = Column(Integer, ForeignKey("project.id"))

#     project = relationship("Project", back_populates="descriptions")

class Education(Base):
    __tablename__ = 'education'
    id = Column(Integer, primary_key=True, index=True)
    degree_name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    college_name = Column(String)
    course_name = Column(String)
    description = Column(Text)
    
class Certificates(Base):
    __tablename__ = 'certificates'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completedOn = Column(Text)
    isActive = Column(Boolean, default=True)

class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    level = Column(Integer)




