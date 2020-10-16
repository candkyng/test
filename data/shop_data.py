import csv
import os


class ShopData:

    CURRENCY = "₹. "
    SUCCESS_MSG_EXPECTED = "Success! Thank you! Your order will be delivered in next few weeks :-)."

    @staticmethod
    def get_csv_lines(filename):
        """
        Read CSV file
        :param filename:
        :return: list of lines of list of values
        """
        current_dir = os.path.dirname(__file__)
        path = current_dir + '\\' + filename
        file = open(file=path)
        return list(csv.reader(file))

    @staticmethod
    def get_data_by_row(csv_lines, data_row):
        """
        Get data by row from CSV
        :param csv_lines:
        :param data_row:
        :return: data dictionary
        """
        header = csv_lines[0]
        row = csv_lines[data_row]
        data = {}
        for col in range(len(header)):
            data[header[col]] = row[col]
        return data

    @staticmethod
    def get_data_all(filename="shop_data.csv"):
        """
        Get data from CSV and convert data to list of dictionary
        :param filename:
        :return:
        """
        csv_lines = ShopData.get_csv_lines(filename)
        data_list = []

        for rownum in range(1, len(csv_lines)):
            data_list.append(ShopData.get_data_by_row(csv_lines, rownum))
        return data_list


