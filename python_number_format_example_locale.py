# Import locale library for formatting of thousands on Booking (base) Graph
import locale
locale.setlocale(locale.LC_ALL, '')

#Getting Started
#Deploy locale to format a number%d/percent%f/series%s/ assigning to 'y' variable

y = locale.format("%S",Number/CalculationWithSingleOutput, grouping=True)
y = locale.format("%d",Number/CalculationWithSingleOutput, grouping=True)
y = locale.format("%e",Number/CalculationWithSingleOutput, grouping=True)




#More on locale formatting library https://docs.python.org/2/library/locale.html
