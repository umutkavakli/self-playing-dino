from utils import balance_dataset, split_images

SOURCE_UP = './source/UP/'
SOURCE_DOWN = './source/DOWN/'
SOURCE_GROUND = './source/GROUND/'

TRAINING_DIR_UP = './images/train/UP/'
TRAINING_DIR_DOWN = './images/train/DOWN/'
TRAINING_DIR_GROUND = './images/train/GROUND/'

TEST_DIR_UP = './images/test/UP/'
TEST_DIR_DOWN = './images/test/DOWN/'
TEST_DIR_GROUND = './images/test/GROUND/'

#balance_dataset(SOURCE_UP, SOURCE_DOWN, SOURCE_GROUND)

split_images(SOURCE_UP, TRAINING_DIR_UP, TEST_DIR_UP)
split_images(SOURCE_DOWN, TRAINING_DIR_DOWN, TEST_DIR_DOWN)
split_images(SOURCE_GROUND, TRAINING_DIR_GROUND, TEST_DIR_GROUND)
