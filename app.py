# importing the packages
import streamlit as st
from PIL import Image


# importingthe files
from eda import eda
from ml import ml

def main():

	menu = ["Home", "Exploratory Data Analysis Section", "Prediction Section", "About"]

	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="Home":

		st.write("# Early Stage heart attack risk predictor app")
		img = Image.open("heart.jpeg")
		st.image(img)

		st.header("Watch this Before using the APP")
		
		video1 = open("webapp_tour.mp4", "rb")
		st.video(video1)

		st.write("""

The data that we use in this particular app contain the features of a newly heart disease patient 
or a diabetic patient.

### DataScource

	- https://archive.ics.uci.edu/ml/datasets/heart+disease

### App Content

	- This app has four sections
	1) Home Page - The page you are currently in

	2) Exploratory Data Analysis - The page in which you will find all the Data Analysis and Visualization Parts

	3) Prediction- The page in which you will be asked to give the information on all the medical aspects
		and we will predict the desired the output

	4) About - This Page is about me

			""")
	elif choice=="Exploratory Data Analysis Section":
		eda()
	elif choice == "Prediction Section":
		ml()
	else:
		st.subheader("About")
		
		st.write("### Adith Sreeram - The Data Guy")
		img = Image.open("asr.jpeg")
		st.image(img)

		st.text("""
		My ambitious dream to become a data scientist is soon to be a reality. Spending hours 
		dlooking for the most appropriate content for you never makes me tired, which will 
		obviously be preceded by long and passionate reading, writing, and prosperity in 
		sharing my wisdom brought me here. 
		As I am pursuing computer engineering, I build computer applications and muscles too.
		I strive to use my energy in data science to make significant contributions to society by 
		tackling complex problems through research and cutting edge technologies.
		Creative problem solver with strong interpersonal skills. Dreaming of taking the world 
		towards a safer and healthier future.
		I love meeting people working on exciting things. If there is any suitable role for me, 
		don't hesitate. I am open to communication on all channels. Let's discuss.
""")
		socials = ["LinkedIn", "Youtube", "Github", "GMail", "Website"]
		linkedin = "http://www.linkedin.com/in/asr373"
		youtube = "https://www.youtube.com/channel/UCo2uuNGUZbHyX3hmuJuraVQ?sub_confirmation=1"
		github = "https://github.com/ASR373"
		mail = "vishra373@gmail.com"
		website = "https://fittechie.in/"
		with st.beta_expander("Links to all my Socials"):
			a = st.selectbox("Socials", socials)
			if a =="LinkedIn":
				st.write(linkedin)
			elif a =="Youtube":
				st.write(youtube)
			elif a =="Github":
				st.write(github)
			elif a=="GMail":
				st.write(mail)
			elif a =="Website":
				st.write(website)
			

			
			


main()
