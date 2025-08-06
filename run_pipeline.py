from scrapers.trend_fetcher import fetch_trends
from scripts.generator import generate_script
from scripts.fetch_images import fetch_images
from scripts.tts_generator import text_to_speech
from scripts.video_maker import make_video
from uploader.upload import upload_video
import os

def main():
    trends = fetch_trends()
    for playlist, topic in trends.items():
        # Generate content
        script = generate_script(topic)
        text_to_speech(script, f"voice_{playlist}.mp3")
        fetch_images(topic, folder=f"images/{playlist}")
        make_video(f"images/{playlist}", f"voice_{playlist}.mp3", f"videos/{playlist}.mp4")
        
        # Upload
        upload_video(
            f"videos/{playlist}.mp4",
            f"{topic} - Allegedly",
            "Automated content. Like & subscribe!",
            PLAYLIST_IDS[playlist]
        )

if __name__ == "__main__":
    main()








#     from apscheduler.schedulers.blocking import BlockingScheduler
# import os
# import logging

# # Import your modules
# from scripts import fetch_topics, generate_script, fetch_images, create_video, upload_youtube

# # Configure logging
# logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# # Define your categories and schedule
# categories = [
#     "News & Gossip",
#     "Conspiracies",
#     "Life Hacks",
#     "Sports",
#     "Technology",
#     "Kids Education",
#     "Untold Stories",
#     "Folktales",
#     "Music"
# ]

# def run_category_pipeline(category):
#     try:
#         logging.info(f'Starting pipeline for {category}')
#         # 1. Fetch topics
#         topics = fetch_topics.fetch_topics(category)
#         if not topics:
#             logging.warning(f'No topics found for {category}')
#             return
#         topic = topics[0]  # pick top topic
#         logging.info(f"Selected topic: {topic}")

#         # 2. Generate script
#         script = generate_script.generate_script(topic, category)
#         with open(f'data/scripts/{category}_{topic}.txt', 'w') as f:
#             f.write(script)

#         # 3. Fetch images
#         images = fetch_images.get_images(topic)
#         # Save images locally or keep URLs for later
#         # For simplicity, assume images are downloaded to images/ folder
#         # and the list is ready for create_video

#         # 4. Generate voiceover
#         voice_path = f"voice/{category}_{topic}.mp3"
#         # Call your voice generator function here
#         # generate_voice(script, voice_path)

#         # 5. Create video
#         output_video = f"videos/{category}_{topic}.mp4"
#         # create_video.create_video(images, voice_path, output_video)

#         # 6. Upload to YouTube
#         # upload_youtube.upload_video(output_video, title, description, tags)

#         # 7. Log success
#         logging.info(f"Successfully processed {category} - {topic}")
#         # TODO: Save logs, update dashboard data

#     except Exception as e:
#         logging.error(f"Error processing {category}: {str(e)}")

# # Setup scheduler
# scheduler = BlockingScheduler()

# # Schedule weekly for each category
# for cat in categories:
#     scheduler.add_job(run_category_pipeline, 'cron', day_of_week='mon-sun', hour=10, args=[cat], id=cat)

# # Run scheduler
# if __name__ == "__main__":
#     print("Starting scheduler...")
#     scheduler.start()