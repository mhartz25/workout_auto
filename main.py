import utils
import static 
import smtplib
import ssl


def main(): 

    legs, biceps, triceps, chest, shoulders, back, corrective = utils.randomizer()

    summed_list = legs + biceps + triceps + chest + shoulders + back + corrective 

    body = utils.format_text(summed_list)

    utils.email(static.sender, static.receiver, static.subject, body)

if __name__ == "__main__":
    main()






