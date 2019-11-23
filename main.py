import photo_parser
import drawer

phrase = input()
stats = photo_parser.main(phrase)
drawer.main(stats)