import cv2
import numpy as np
from moviepy.editor import *
from Components.Speaker import detect_faces_and_speakers, Frames

global Fps


# def crop_to_vertical(input_video_path, output_video_path):
#     detect_faces_and_speakers(input_video_path, "DecOut.mp4")
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
#     cap = cv2.VideoCapture(input_video_path, cv2.CAP_FFMPEG)
#     if not cap.isOpened():
#         print("Error: Could not open video.")
#         return
#
#     original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#
#     vertical_height = int(original_height)
#     vertical_width = int(vertical_height * 9 / 16)
#     print(vertical_height, vertical_width)
#
#     if original_width < vertical_width:
#         print("Error: Original video width is less than the desired vertical width.")
#         return
#
#     x_start = (original_width - vertical_width) // 2
#     x_end = x_start + vertical_width
#     print(f"start and end - {x_start} , {x_end}")
#     print(x_end - x_start)
#     half_width = vertical_width // 2
#
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(output_video_path, fourcc, fps, (vertical_width, vertical_height))
#     global Fps
#     Fps = fps
#     print(fps)
#     count = 0
#     for _ in range(total_frames):
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: Could not read frame.")
#             break
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#         if len(faces) > -1:
#             # When no faces are detected, fallback to face data from Frames
#             if len(faces) == 0:
#                 if len(Frames) > 0:
#                     if count < len(Frames):
#                         (x, y, w, h) = Frames[count]
#                     else:
#                         print("No corresponding frame in Frames for current count, using last available frame.")
#                         (x, y, w, h) = Frames[-1]
#                 else:
#                     # If Frames is empty, default to current face values
#                     x, y, w, h = 0, 0, 0, 0
#
#             # Retrieve face data from Frames for adjustment
#             if len(Frames) == 0:
#                 print("No face frames available.")
#             else:
#                 if count >= len(Frames):
#                     count = len(Frames) - 1
#                 try:
#                     (X, Y, W, H) = Frames[count]
#                 except Exception as e:
#                     print("Error accessing Frames:", e)
#                     try:
#                         (X, Y, W, H) = Frames[count][0]
#                         print("Using fallback:", Frames[count][0])
#                     except Exception as e2:
#                         print("Fallback also failed:", e2)
#                         (X, Y, W, H) = (0, 0, 0, 0)
#
#             # Use detected faces to adjust crop if one lies within the current face bounds
#             for f in faces:
#                 x1, y1, w1, h1 = f
#                 center = x1 + w1 // 2
#                 if center > X and center < X + W:
#                     x = x1
#                     y = y1
#                     w = w1
#                     h = h1
#                     break
#
#             centerX = x + (w // 2)
#             print("Center X:", centerX)
#             print("Offset:", x_start - (centerX - half_width))
#             if count == 0 or (x_start - (centerX - half_width)) < 1:
#                 # If the difference from the previous frame is low, keep the previous crop
#                 pass
#             else:
#                 x_start = centerX - half_width
#                 x_end = centerX + half_width
#
#                 # Adjust cropping if the cropped width doesn't match
#                 cropped_frame = frame[:, x_start:x_end]
#                 if int(cropped_frame.shape[1]) != x_end - x_start:
#                     if x_end < original_width:
#                         x_end += int(cropped_frame.shape[1]) - (x_end - x_start)
#                         if x_end > original_width:
#                             x_start -= int(cropped_frame.shape[1]) - (x_end - x_start)
#                     else:
#                         x_start -= int(cropped_frame.shape[1]) - (x_end - x_start)
#                         if x_start < 0:
#                             x_end += int(cropped_frame.shape[1]) - (x_end - x_start)
#                     print("Frame size inconsistent")
#                     print("New width:", x_end - x_start)
#         count += 1
#         cropped_frame = frame[:, x_start:x_end]
#         if cropped_frame.shape[1] == 0:
#             x_start = (original_width - vertical_width) // 2
#             x_end = x_start + vertical_width
#             cropped_frame = frame[:, x_start:x_end]
#
#         print("Cropped frame shape:", cropped_frame.shape)
#         out.write(cropped_frame)
#
#     cap.release()
#     out.release()
#     print("Cropping complete. The video has been saved to", output_video_path, "Total frames processed:", count)

def crop_to_vertical(input_video_path, output_video_path):
    detect_faces_and_speakers(input_video_path, "DecOut.mp4")
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(input_video_path, cv2.CAP_FFMPEG)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    vertical_height = int(original_height)
    vertical_width = int(vertical_height * 9 / 16)
    print(vertical_height, vertical_width)

    if original_width < vertical_width:
        print("Error: Original video width is less than the desired vertical width.")
        return

    x_start = (original_width - vertical_width) // 2
    x_end = x_start + vertical_width
    print(f"start and end - {x_start} , {x_end}")
    print(x_end - x_start)
    half_width = vertical_width // 2

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (vertical_width, vertical_height))
    global Fps
    Fps = fps
    print(fps)
    count = 0
    for _ in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Prepare a fallback face from Frames if available
        if len(Frames) > 0:
            fallback_face = Frames[min(count, len(Frames) - 1)]
        else:
            fallback_face = (0, 0, 0, 0)

        if len(faces) == 0:
            # No faces detected: use fallback face data
            x, y, w, h = fallback_face
        else:
            # Retrieve face data from Frames for adjustment if available
            if len(Frames) != 0:
                if count >= len(Frames):
                    count = len(Frames) - 1
                try:
                    (X, Y, W, H) = Frames[count]
                except Exception as e:
                    print("Error accessing Frames:", e)
                    try:
                        (X, Y, W, H) = Frames[count][0]
                        print("Using fallback:", Frames[count][0])
                    except Exception as e2:
                        print("Fallback also failed:", e2)
                        (X, Y, W, H) = (0, 0, 0, 0)
            else:
                X, Y, W, H = (0, 0, 0, 0)

            face_found = False
            # Use detected faces to adjust crop if one lies within the current face bounds
            for f in faces:
                x1, y1, w1, h1 = f
                center = x1 + w1 // 2
                if center > X and center < X + W:
                    x = x1
                    y = y1
                    w = w1
                    h = h1
                    face_found = True
                    break
            if not face_found:
                x, y, w, h = fallback_face

        centerX = x + (w // 2)
        print("Center X:", centerX)
        print("Offset:", x_start - (centerX - half_width))
        if count == 0 or (x_start - (centerX - half_width)) < 1:
            # If the difference from the previous frame is low, keep the previous crop
            pass
        else:
            x_start = centerX - half_width
            x_end = centerX + half_width

            # Adjust cropping if the cropped width doesn't match
            cropped_frame = frame[:, x_start:x_end]
            if int(cropped_frame.shape[1]) != x_end - x_start:
                if x_end < original_width:
                    x_end += int(cropped_frame.shape[1]) - (x_end - x_start)
                    if x_end > original_width:
                        x_start -= int(cropped_frame.shape[1]) - (x_end - x_start)
                else:
                    x_start -= int(cropped_frame.shape[1]) - (x_end - x_start)
                    if x_start < 0:
                        x_end += int(cropped_frame.shape[1]) - (x_end - x_start)
                print("Frame size inconsistent")
                print("New width:", x_end - x_start)
        count += 1
        cropped_frame = frame[:, x_start:x_end]
        if cropped_frame.shape[1] == 0:
            x_start = (original_width - vertical_width) // 2
            x_end = x_start + vertical_width
            cropped_frame = frame[:, x_start:x_end]

        print("Cropped frame shape:", cropped_frame.shape)
        out.write(cropped_frame)

    cap.release()
    out.release()
    print("Cropping complete. The video has been saved to", output_video_path, "Total frames processed:", count)


def combine_videos(video_with_audio, video_without_audio, output_filename):
    try:
        # Load video clips
        clip_with_audio = VideoFileClip(video_with_audio)
        clip_without_audio = VideoFileClip(video_without_audio)

        audio = clip_with_audio.audio
        combined_clip = clip_without_audio.set_audio(audio)

        global Fps
        combined_clip.write_videofile(output_filename, codec='libx264', audio_codec='aac', fps=Fps, preset='medium',
                                      bitrate='3000k')
        print(f"Combined video saved successfully as {output_filename}")

    except Exception as e:
        print(f"Error combining video and audio: {str(e)}")


if __name__ == "__main__":
    input_video_path = r'Out.mp4'
    output_video_path = 'Croped_output_video.mp4'
    final_video_path = 'final_video_with_audio.mp4'
    detect_faces_and_speakers(input_video_path, "DecOut.mp4")
    crop_to_vertical(input_video_path, output_video_path)
    combine_videos(input_video_path, output_video_path, final_video_path)