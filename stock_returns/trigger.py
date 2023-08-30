def trigger():

    query = 'create trigger '
    query += 'update_portfolio '
    query += 'after insert on '
    query += 'transaction_history '
    query += 'for each row '
    query += 'begin '
    query += 'if (new.position_type > 0 and new.action > 0) then '
    query += 'INSERT INTO '
    query += 'portfolio '
    query += 'values ' 
    query += '( '
    query += 'new.ticker, ' 
    query += 'new.position_type, ' 
    query += 'new.no_shares,  '
    query += 'new.at_price,  '
    query += 'new.at_price, '
    query += 'new.at_price * new.no_shares, '
    query += '0, '
    query += '0 '
    query += ')  '
    query += 'ON DUPLICATE KEY UPDATE '
    query += 'position = position + new.no_shares, '
    query += 'last_price = new.at_price, '
    query += 'cost_basis = ( '
    query += '((position - new.no_shares) * cost_basis) '
    query += '+ new.no_shares * last_price '
    query += ') / position, '
    query += 'current_value = position * new.at_price, '
    query += 'realized_profit = realized_profit, '
    query += 'gain = 100.0 * ( '
    query += 'current_value + realized_profit - (position * cost_basis) '
    query += ') / (position * cost_basis); '
    query += 'elseif (new.position_type > 0 and new.action < 0) then '
    query += 'UPDATE portfolio SET '
    query += 'position = position - new.no_shares, '
    query += 'last_price = new.at_price, '
    query += 'cost_basis = cost_basis, '
    query += 'current_value = position * new.at_price, '
    query += 'realized_profit = realized_profit + (new.no_shares * new.at_price), '
    query += 'gain = 100.0 * ( '
    query += 'current_value + realized_profit - (position * cost_basis) '
    query += ') / (position * cost_basis) '
    query += 'where position_type = new.position_type and ticker = new.ticker; '
    query += 'elseif (new.position_type < 0 and new.action < 0) then '
    query += 'INSERT INTO '
    query += 'portfolio '
    query += 'values '
    query += '( '
    query += 'new.ticker, '
    query += 'new.position_type, '
    query += 'new.no_shares * -1.0, '
    query += 'new.at_price, '
    query += 'new.at_price, '
    query += 'new.at_price * new.no_shares * -1.0, '
    query += 'new.at_price * new.no_shares, '
    query += '0 '
    query += ') '
    query += 'ON DUPLICATE KEY UPDATE  '
    query += 'position = position - new.no_shares, '
    query += 'last_price = new.at_price, '
    query += 'cost_basis = ( '
    query += '(-1.0 * (position + new.no_shares) * cost_basis) '
    query += '+ (new.no_shares * new.at_price) '
    query += ') / position * -1.0, '
    query += 'current_value = position * new.at_price, '
    query += 'realized_profit = realized_profit + (new.at_price * new.no_shares), '
    query += 'gain = 100.0 * (realized_profit + current_value) / realized_profit; '
    query += 'elseif (new.position_type < 0 and new.action > 0) then '
    query += 'UPDATE portfolio SET '
    query += 'position = position + new.no_shares, '
    query += 'last_price = new.at_price, '
    query += 'cost_basis = cost_basis, '
    query += 'current_value = position * new.at_price, '
    query += 'realized_profit = realized_profit - (new.at_price * new.no_shares), '
    query += 'gain = 100.0 * (realized_profit + current_value) / realized_profit '
    query += 'where position_type = new.position_type and ticker = new.ticker; '
    query += 'end if; '
    query += 'end; '

    return query