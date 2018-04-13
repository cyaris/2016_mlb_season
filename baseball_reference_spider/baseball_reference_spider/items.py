# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaseballReferenceItem(scrapy.Item):

    boxscore_url = scrapy.Field()
    away_team = scrapy.Field()
    away_team_runs = scrapy.Field()
    away_team_hits = scrapy.Field()
    away_team_errors = scrapy.Field()
    home_team = scrapy.Field()
    home_team_runs = scrapy.Field()
    home_team_hits = scrapy.Field()
    home_team_errors = scrapy.Field()
    date = scrapy.Field()
    start_time = scrapy.Field()
    attendance = scrapy.Field()
    venue = scrapy.Field()
    game_duration = scrapy.Field()
    game_type = scrapy.Field()
    field_type = scrapy.Field()
    other_info_string = scrapy.Field()
