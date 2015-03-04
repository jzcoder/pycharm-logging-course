# mortgage library
#
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler('library.log'))

def get_current_rate(years):
    logging.debug('Fetching current interest rate for %d years' % years)
    rate = 5.3   # Stub external service call
    logging.debug('Service returned interest rate %f' % rate)
    return rate

def get_monthly_payment(principal, years):
    logging.info("Calling mortgage calculator")

    if years > 50:
        logging.warn('Term greater than 50 years')

    mon_rate = get_current_rate(years)/1200
    payments = years * 12
    logging.debug('Number of monthly payments %d' % payments)
    result = principal * (mon_rate/(1-math.pow((1+mon_rate), -payments)))

    logging.debug("Calculated result is %f" % result)
    logging.debug("Leaving mortgage calculator")
    return result