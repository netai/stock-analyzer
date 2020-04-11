def find_candle_pattern(stock_data):
    candle_1 = stock_data[0].StockDayReport
    candle_2 = stock_data[1].StockDayReport
    candle_3 = stock_data[2].StockDayReport
    candle_4 = stock_data[3].StockDayReport
    
    DOJI_SIZE = 0.1
    #Doji Pattern
    doji = (abs(candle_1.open_price - candle_1.close_price) <= (candle_1.high_price - candle_1.low_price) * DOJI_SIZE)
    #Hammer Pattern
    hammer = (((candle_1.high_price - candle_1.low_price) > 3*(candle_1.open_price - candle_1.close_price)) & \
        ((candle_1.close_price - candle_1.low_price)/(.001 + candle_1.high_price - candle_1.low_price) > 0.6) & \
            ((candle_1.open_price - candle_1.low_price)/(.001 + candle_1.high_price - candle_1.low_price) > 0.6))
    #Inverted Hammer Pattern
    inverted_hammer = (((candle_1.high_price - candle_1.low_price) > 3*(candle_1.open_price - candle_1.close_price)) & \
        ((candle_1.high_price - candle_1.close_price)/(.001 + candle_1.high_price - candle_1.low_price) > 0.6) & \
            ((candle_1.high_price - candle_1.open_price)/(.001 + candle_1.high_price - candle_1.low_price) > 0.6))
    #Bullish Reversal Pattern
    bullish_reversal = (candle_3.open_price > candle_3.close_price) & (candle_2.open_price > candle_2.close_price) & doji
    #Bearish Reversal Pattern
    bearish_reversal = (candle_3.open_price < candle_3.close_price) & (candle_2.open_price < candle_2.close_price) & doji
    #Evening Star Pattern
    evening_star = (candle_3.close_price > candle_3.open_price) & (min(candle_2.open_price, candle_2.close_price) > candle_3.close_price) & \
        (candle_1.open_price < min(candle_2.open_price, candle_2.close_price)) & (candle_1.close_price < candle_1.open_price)
    #Morning Star Pattern
    morning_star = (candle_3.close_price < candle_3.open_price) & (min(candle_2.open_price, candle_2.close_price) < candle_3.close_price) & \
        (candle_1.open_price > min(candle_2.open_price, candle_2.close_price)) & (candle_1.close_price > candle_1.open_price )
    #Shooting Star Bearish Pattern
    shooting_star_bearish = (candle_2.open_price < candle_2.close_price) & (candle_1.open_price > candle_2.close_price) & \
        ((candle_1.high_price - max(candle_1.open_price, candle_1.close_price)) >= abs(candle_1.open_price - candle_1.close_price) * 3) & \
            ((min(candle_1.close_price, candle_1.open_price) - candle_1.low_price ) <= abs(candle_1.open_price - candle_1.close_price)) & inverted_hammer
    #Shooting Star Bullish Pattern
    shooting_star_bullish = (candle_2.open_price > candle_2.close_price) & (candle_1.open_price < candle_2.close_price) & \
        ((candle_1.high_price - max(candle_1.open_price, candle_1.close_price)) >= abs(candle_1.open_price - candle_1.close_price) * 3) & \
            ((min(candle_1.close_price, candle_1.open_price) - candle_1.low_price ) <= abs(candle_1.open_price - candle_1.close_price)) & inverted_hammer
    #Bearish Harami Pattern
    bearish_harami = (candle_2.close_price > candle_2.open_price) & (candle_1.open_price > candle_1.close_price) & \
        (candle_1.open_price <= candle_2.close_price) & (candle_2.open_price <= candle_1.close_price) & \
            ((candle_1.open_price - candle_1.close_price) < (candle_2.close_price - candle_2.open_price ))
    #Bullish Harami Pattern
    bullish_harami = (candle_2.open_price > candle_2.close_price) & (candle_1.close_price > candle_1.open_price) & \
        (candle_1.close_price <= candle_2.open_price) & (candle_2.close_price <= candle_1.open_price) & \
            ((candle_1.close_price - candle_1.open_price) < (candle_2.open_price - candle_2.close_price))
    #Bearish Engulfing Pattern
    bearish_engulfing = ((candle_2.close_price > candle_2.open_price) & (candle_1.open_price > candle_1.close_price)) & \
        ((candle_1.open_price >= candle_2.close_price) & (candle_2.open_price >= candle_1.close_price)) & \
            ((candle_1.open_price - candle_1.close_price) > (candle_2.close_price - candle_2.open_price ))
    #Bullish Engulfing Pattern
    bullish_engulfing = (candle_2.open_price > candle_2.close_price) & (candle_1.close_price > candle_1.open_price) & \
        (candle_1.close_price >= candle_2.open_price) & (candle_2.close_price >= candle_1.open_price) & \
            ((candle_1.close_price - candle_1.open_price) > (candle_2.open_price - candle_2.close_price ))
    #Piercing Line Bullish Pattern
    piercing_line_bullish = (candle_2.close_price < candle_2.open_price) & (candle_1.close_price > candle_1.open_price) & \
        (candle_1.open_price < candle_2.low_price) & (candle_1.close_price > candle_2.close_price) & \
            (candle_1.close_price > ((candle_2.open_price + candle_2.close_price)/2)) & (candle_1.close_price < candle_2.open_price)
    #Hanging Man Bullish Pattern
    hanging_man_bullish = (candle_2.close_price < candle_2.open_price) & (candle_1.open_price < candle_2.low_price) & \
        (candle_1.close_price > ((candle_2.open_price + candle_2.close_price)/2)) & (candle_1.close_price < candle_2.open_price) & hammer
    #Hanging man Bearish Pattern
    hanging_man_bearish = (candle_2.close_price > candle_2.open_price) & (candle_1.close_price > ((candle_2.open_price + candle_2.close_price)/2)) & \
        (candle_1.close_price < candle_2.open_price) & hammer

    candle_pattern_name = []
    candle_score = 0
    
    if doji:
        candle_pattern_name.append('doji')
    if hammer:
        candle_pattern_name.append('hammer')
    if inverted_hammer:
        candle_pattern_name.append('inverted_hammer')
    if bullish_reversal:
        candle_pattern_name.append('bullish_reversal')
        candle_score = candle_score + 1
    if bearish_reversal:
        candle_pattern_name.append('bearish_reversal')
        candle_score = candle_score - 1
    if evening_star:
        candle_pattern_name.append('evening_star')
        candle_score = candle_score - 1
    if morning_star:
        candle_pattern_name.append('morning_star')
        candle_score = candle_score + 1
    if shooting_star_bearish:
        candle_pattern_name.append('shooting_star_bearish')
        candle_score = candle_score - 1
    if shooting_star_bullish:
        candle_pattern_name.append('shooting_star_bullish')
        candle_score = candle_score + 1
    if bearish_harami:
        candle_pattern_name.append('bearish_harami')
        candle_score = candle_score - 1
    if bullish_harami:
        candle_pattern_name.append('bullish_harami')
        candle_score = candle_score + 1
    if bearish_engulfing:
        candle_pattern_name.append('bearish_engulfing')
        candle_score = candle_score - 1
    if bullish_engulfing:
        candle_pattern_name.append('bullish_engulfing')
        candle_score = candle_score + 1
    if piercing_line_bullish:
        candle_pattern_name.append('piercing_line_bullish')
        candle_score = candle_score + 1
    if hanging_man_bullish:
        candle_pattern_name.append('hanging_man_bullish')
        candle_score = candle_score + 1
    if hanging_man_bearish:
        candle_pattern_name.append('hanging_man_bearish')
        candle_score = candle_score - 1

    return candle_pattern_name, candle_score