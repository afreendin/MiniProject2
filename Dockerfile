FROM python:3

ADD HelperFunctions /HelperFunctions
ADD DescriptiveStatisticsFunction /DescriptiveStatisticsFunction
ADD UnitTest /UnitTest

CMD [ "python", "./UnitTest/UnitTest.py" ]