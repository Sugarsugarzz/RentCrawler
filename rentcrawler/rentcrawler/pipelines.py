import csv
from scrapy.exceptions import DropItem


class CsvPipeline(object):

    def process_item(self, item, spider):

        if item['house_city'] == '北京':
            with open('LianjiaBj.csv', 'a+', encoding='utf-8') as f:
                csv_writer = csv.writer(f, delimiter=',')
                csv_writer.writerow([item['house_city'], item['house_title'], item['house_location'],
                                     item['house_size'], item['house_orient'], item['house_type'],
                                     item['house_time'], item['house_price'], item['house_images'],
                                     item['house_url']])
        elif item['house_city'] == '上海':
            with open('LianjiaSh.csv', 'a+', encoding='utf-8') as f:
                csv_writer = csv.writer(f, delimiter=',')
                csv_writer.writerow([item['house_city'], item['house_title'], item['house_location'],
                                     item['house_size'], item['house_orient'], item['house_type'],
                                     item['house_time'], item['house_price'], item['house_images'],
                                     item['house_url']])
        elif item['house_city'] == '广州':
            with open('LianjiaGz.csv', 'a+', encoding='utf-8') as f:
                csv_writer = csv.writer(f, delimiter=',')
                csv_writer.writerow([item['house_city'], item['house_title'], item['house_location'],
                                     item['house_size'], item['house_orient'], item['house_type'],
                                     item['house_time'], item['house_price'], item['house_images'],
                                     item['house_url']])
        elif item['house_city'] == '深圳':
            with open('LianjiaSz.csv', 'a+', encoding='utf-8') as f:
                csv_writer = csv.writer(f, delimiter=',')
                csv_writer.writerow([item['house_city'], item['house_title'], item['house_location'],
                                     item['house_size'], item['house_orient'], item['house_type'],
                                     item['house_time'], item['house_price'], item['house_images'],
                                     item['house_url']])
        elif item['house_city'] == '成都':
            with open('LianjiaCd.csv', 'a+', encoding='utf-8') as f:
                csv_writer = csv.writer(f, delimiter=',')
                csv_writer.writerow([item['house_city'], item['house_title'], item['house_location'],
                                     item['house_size'], item['house_orient'], item['house_type'],
                                     item['house_time'], item['house_price'], item['house_images'],
                                     item['house_url']])

        return item





