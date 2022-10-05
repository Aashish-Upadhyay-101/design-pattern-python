"""Basic video exporter example"""

from abc import ABC, abstractmethod
import pathlib

class VideoExporter(ABC):
    """Basic representation of video exporting codec"""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video for exporting"""
    
    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports a video to a folder"""


class HighQualityVideoExporter(VideoExporter):
    """Export high quality video"""

    def prepare_export(self, video_data):
        print(f"Preparing {video_data} to export for HIGH QUALITY EXPORT")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting HIGH QUALITY video to {folder}")


class MediumQualityVideoExporter(VideoExporter):
    """Export medium quality video"""

    def prepare_export(self, video_data):
        print(f"Preparing {video_data} to export for MEDIUM QUALITY EXPORT")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting MEDIUM QUALITY video to {folder}")


class LowQualityVideoExporter(VideoExporter):
    """Export low quality video"""

    def prepare_export(self, video_data):
        print(f"Preparing {video_data} to export for LOW QUALITY EXPORT")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting LOW QUALITY video to {folder}")


class AudioExporter(ABC):
    """Basic representation of audio exporting codec"""

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio for exporting"""
    
    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports a audio to a folder"""


class HighQualityAudioExporter(AudioExporter):
    """Export HIGH quality audio"""

    def prepare_export(self, audio_data):
        print(f"Preparing {audio_data} to export for HIGH QUALITY EXPORT")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting LOW QUALITY audio to {folder}")


class MediumQualityAudioExporter(AudioExporter):
    """Export MEDIUM quality audio"""

    def prepare_export(self, audio_data):
        print(f"Preparing {audio_data} to export for MEDIUM QUALITY EXPORT")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting MEDIUM QUALITY audio to {folder}")


class LowQualityAudioExporter(AudioExporter):
    """Export LOW quality audio"""

    def prepare_export(self, audio_data):
        print(f"Preparing {audio_data} to export for LOW QUALITY EXPORT")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting LOW QUALITY audio to {folder}")


class ExporterFactory(ABC):
    """
    Factory that represents a combination of video and audio codec.
    The factory doesn't maintain any of the instances it creates.
    """

    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance"""

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter instance"""


class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing a high quality audio and video export"""

    def get_video_exporter(self) -> VideoExporter:
        return HighQualityVideoExporter()
    
    def get_audio_exporter(self) -> AudioExporter:
        return HighQualityAudioExporter()
    

class MediumQualityExporter(ExporterFactory):
    """Factory aimed to providing a medium quality audio and video export"""

    def get_video_exporter(self) -> VideoExporter:
        return MediumQualityVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return MediumQualityAudioExporter()


class LowQualityExporter(ExporterFactory):
    """Factory aimed to providing a low quality audio and video export"""

    def get_video_exporter(self) -> VideoExporter:
        return LowQualityVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return LowQualityAudioExporter()


def read_exporter():

    quality_factory = {
        "low": LowQualityExporter(),
        "medium": MediumQualityExporter(),
        "high": HighQualityExporter(),
    }

    export_quality = input("Enter the desired quality -> (low, medium, high): ")
    if export_quality in quality_factory:
        return quality_factory[export_quality]
    else:
        raise ValueError("Unknown quality format")
       
    
    

def main() -> None:
    try:
        exporter = read_exporter()
        video_exporter = exporter.get_video_exporter()
        audio_exporter = exporter.get_audio_exporter()

        video_exporter.prepare_export("Video Placeholder")
        audio_exporter.prepare_export("Audio Placeholder")
        
        folder_path = pathlib.Path("usr/tmp/video")

        video_exporter.do_export(folder_path)
        audio_exporter.do_export(folder_path)
    except ValueError as e:
        print(e)
    

if __name__ == "__main__":
    main()