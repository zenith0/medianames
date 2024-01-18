import unittest
from medianames.utils.helper_functions import *


class TestHelperFunctions(unittest.TestCase):
  def test_clean_folder_name(self):
    complex_folder_name="Spiderman.Far.from.Home.2019.German.AC3.1080p.BluRay.x265-GTF"
    clean_folder_name_result = clean_folder_name(complex_folder_name)
    self.assertEqual("Spiderman Far from Home", clean_folder_name_result)

    complex_folder_name="Star Trek - Discovery"
    clean_folder_name_result = clean_folder_name(complex_folder_name)
    self.assertEqual("Star Trek - Discovery", clean_folder_name_result)

    complex_folder_name="S04"
    clean_folder_name_result = clean_folder_name(complex_folder_name)
    self.assertEqual("S04", clean_folder_name_result)

    complex_folder_name="Star.Wars.The.Bad.Batch.S01E01.GERMAN.DL.1080P.WEB.H264-WAYNE"
    clean_folder_name_result = clean_folder_name(complex_folder_name)
    self.assertEqual("Star Wars The Bad Batch-S01E01", clean_folder_name_result)

    # sorry swat fans
    complex_folder_name="S.W.A.T - S05"
    clean_folder_name_result = clean_folder_name(complex_folder_name)
    self.assertEqual("S W A T - S05", clean_folder_name_result)

    complex_folder_name="Attack.on.Titan.E12.Die.Wunde.-.Schlacht.um.Bezirk.Trost.Teil.8.German.2013.ANiME.DL.720p.BluRay.x264-STARS"
    clean_folder_name_result = clean_folder_name(complex_folder_name)
    self.assertEqual("Attack on Titan E12 Die Wunde - Schlacht um Bezirk Trost Teil 8 German", clean_folder_name_result)

  def test_is_episode(self):
    self.assertTrue(is_episode("Star Wars The Bad Batch-S01E01"))
    self.assertTrue(is_episode("Attack on Titan E12 Die Wunde"))
    self.assertFalse(is_episode("Star Trek - Discovery"))
    self.assertFalse(is_episode("S04"))
    self.assertFalse(is_episode("S W A T - S05"))
    
  def test_get_season(self):
    self.assertEqual("S01", get_season("Star Wars The Bad Batch-S01E01"))

  def test_get_show(self):
    self.assertEqual("Star Wars The Bad Batch", get_show("Star Wars The Bad Batch-S01E01"))
    self.assertEqual("S W A T", get_show("S W A T-S06"))
    self.assertEqual("S W A T", get_show("S W A T - S06"))
    self.assertEqual("Reacher", get_show('reacher.s02e07.german.dl.1080p.web.h264-wayne.mkv'))



  def test_is_season(self):
    self.assertTrue(is_season('S W A T - S05'))
    self.assertTrue(is_season('S W A T - S05E02'))
    self.assertTrue(is_season('reacher.s02e07.german.dl.1080p.web.h264-wayne.mkv'))



if __name__ == '__main__':
    unittest.main()