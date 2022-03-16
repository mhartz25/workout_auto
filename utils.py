from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from smtplib import SMTP
import smtplib
import textwrap
import static
import ssl
import random



#Function that will intiate the email



    




#Function that will randomize the workout
#how am I going to randomize each week's workout without having to manually run the script and change parameters

def randomizer():
    '''this function will take a workout type as an input(E.g. biceps, legs, shoulders, etc)
    
        and return a list? that will have the name of X number of exercises in the workout

        looking for between 3-6 exercises in each workout


    '''
    legs_workouts = random.sample(static.legs_exercises, k = static.exercises_per_workout.get('legs'))

    bicep_workouts = random.sample(static.bicep_exercises, k = static.exercises_per_workout.get('biceps'))

    tricep_workouts = random.sample(static.tricep_exercises, k = static.exercises_per_workout.get('triceps'))

    chest_workouts = random.sample(static.chest_exercises, k = static.exercises_per_workout.get('chest'))

    shoulders_workouts = random.sample(static.shoulders_exercises, k = static.exercises_per_workout.get('shoulders'))

    back_workouts = random.sample(static.back_exercises, k = static.exercises_per_workout.get('back'))

    corrective_workouts = random.sample(static.corrective_exercises, k = static.exercises_per_workout.get('corrective'))

    return legs_workouts, bicep_workouts, tricep_workouts, chest_workouts, shoulders_workouts, back_workouts, corrective_workouts



def format_text(summed_list):
    '''Format the random text'''
   
    string = f'''Legs: {summed_list[0:3]}\n\n
    
                Biceps: {summed_list[4:8]}\n\n
                
                Triceps: {summed_list[8:12]}\n\n
                
                Chest: {summed_list[12:16]} \n\n
                
                Shoulders: {summed_list[16:20]} \n\n
                
                Back: {summed_list[20:24]} \n\n
                
                Correctives: {summed_list[24:26]}'''

    return string 
def email(sender, receiver, subject, body):
    """
    This function sends an email using Bloomberg's SMTP server
    :param to_email: str or list, 'recipient1@bloomberg.net'
    :param from_email: str , 'youremail@bloomberg.net'
    :param subject: str, 'Automated Message'
    :param body: str, 'Body body body body.'
    :param file_name, 'Name of the file'
    :param reply_to: str
    :param report: csv to be sent to vendors
    :param email_format: str, 'plain' or 'html'
    :return: None
    """

    # Create a secure SSL context
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login("pikrust2022+python@gmail.com", static.email_lock)


        msg = f"Subject: {subject} \n\n {body}"

        smtp.sendmail(sender , receiver, msg)