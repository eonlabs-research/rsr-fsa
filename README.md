# OVERVIEW
`fsa_simulation.py` simulate a **funded sub-account (FSA) partnership** between EonLabs and Researcher (RSR). A worst-but-still-unfailing performance (**WBSUP**) is always assumed in all FSAs. **WBSUP** is perhaps the most important concept to consider. So please don't hesitate to contact EonLabs for more information if you have any questions.

- `fsa_simulation.py` will generate a table with ten (10) columns and twenty-five (25) rows. Each row represents a single month, from the 0th to the 24th. Each column's significance is detailed in #what-each-colum-means?
- They comprise information such as initial and subsequent fund injections, month start and end balances, realized profit, and settled RSR payment. Profit is the only thing that is imitated, not loss.
- The realized profit delay may be adjusted from one to two months. Anything longer than a two-month period is not evaluated since it would surpass the WBSUP level, causing the requirement to fail.

`fsa_simulation.py` default parameter settings are not fixed in stone. Researchers (RSR) are urged to experiment with the parameters until they discover an appropriate set of settings to submit to EonLabs for consideration.

# WORST-BUT-STILL-UNFAILING PERFORMANCE (WBSUP)
**WBSUP** is used to evaluate the trading performance of researchers (RSR). It is built in such a manner that everyone understands what is anticipated before trading starts.

## DEFINITION
**WBSUP** means that a _**minimal**_ **EXTENDED ASSET VALUE**, "R%" (e.g. {d[rateR]}), must be gained within an agreed period of time, "T" (e.g. {d[timeT]} days). Note that "R%" is evaluated dynamically and is relative to the risk taken recently. The maximum allowed downside risk to be taken by RSR is "-R%"

## MAXIMUM ALLOWED DOWNSIDE RISK FROM ALL-TIME HIGH ("A")
If "-R%" = -{d[rateR]}, it means that the maximum drawdown cannot be larger than the multiple of {d[rateR]} from [#ffff00][i]any[/][/] all-time high on the equity curve of total asset value.

### FOR EXAMPLE
Let's say point A ("A") is an all-time high on equity curve. "-R%" is the extent of maximum drawdown between "A" and before "A" is surpassed again. "-R%" cannot exceed an agreed value (e.g. -{d[rateR]}) during drawdown. If "-R%" exceeded the agreed value, WBSUP is considered failed.

## MAXIMUM ALLOWED TIME TO REACH NEXT ALL-TIME HIGH ("B")
Let's continue our illustration from the example above. Let's say point B ("B") is the next all-time high on equity curve, where "B"="A"*(1+"R%"). The value of "R%" in the equation equals the recent drawdown "-R%", which happens between "A" and "B". Apparently, the "-R%" value might vary as long as it doesn't exceed the maximum allowed downside risk from "A". WBSUP requires that RSR balance must attain "B" within certain agreed period ("T"). If "B" cannot be attained within that period, WBSUP is considered failed.

### FOR EXAMPLE
To illustrate, let's say "T" is agreed by EonLabs and RSR to be {d[timeT]} days. If there is a [#00ffff]5.8%[/] drawdown from an all-time high ("A" = 48390 BUSD), it means the equity curve is hitting a trough (80000*(1-0.058) = 75360 BUSD).
WBSUP requires that a minimal EXTENDED ASSET VALUE ("A"*"R%" = 80000*0.058 = 4640 BUSD) must be gained within {d[timeT]} days after the day when "A" happens. In other words, the equity balance of total asset value must attain or exceed "B" ("A"*(1+"R%") = 80000*(1+0.058) = 84640 BUSD) within {d[timeT]} days after the day when "A" happens.

# What Each Column Means?
[#BB8FCE][b]EQUITY BALANCE MONTH START[/][/] ("X") - The Researcher (RSR) is responsible for trading an agreed number of funded sub-accounts (FSAs). "X" is the asset value of all FSAs at the beginning of the month. "X" is denominated in stablecoin (e.g. BUSD). RSR can freely rebalance the funds among the FSAs at any time.

[red][b]EXTENDED ASSET VALUE[/][/] ("A"*"R%") - It means trading profit. Here we simulate "R%" as a fixed value {d[rateR]} that is attained every {d[freqM]} months. During LIVE trading, EonLabs capture Margin Balance hourly from Binance. The captured data includes realized and unrealized profit and loss (PnL). Only realized profit is counted towards "A" & "B". But momentary unrealized losses will be counted toward drawdown of "-R%". Therefore it is important for an RSR to size each trading position carefully so that the sum of all losses ([#ffff00][i]including unrealzed ones[/][/]) since the most recent all-time high asset value ("A") in all the funded sub-accounts (FSA) that the RSR manages the does not exceed the the multiple of {d[rateR]} and "A".

[#00FF00][b]RSR TECHNO FEE[/][/] ("A"*"R%"*"S%") - RSR TECHNO FEE is the multiple of EXTENDED ASSET VALUE ("A"*"R%") and "S%" {d[rateS]} and it is payable monthly by EonLabs to RSR. It is payable to RSR as long as WBSUP is maintained by RSR. Interim profit and loss (realized & unrealized) is monitored to assess WBSUP only. Interim P&L will not be used to calculate RSR TECHNO FEE, which is calculated on the month-end settlement date only.
[#00FF00][b]RSR ACCRUED TECHNO FEE[/][/] - Cumulative RSR TECHNO FEE that RSR received from EonLabs.
[#00FF00][b]RSR BLADE REDUCED LICENSE FEE[/][/] ("D") - "D" is the difference between the license fee ({d[licnZ]} BUSD) and RSR ACCRUED FEE. It is a one-time fee payable by EonLabs to RSR not later than the {d[timeL]}th month. However, EonLabs is entitled to settle the payment of "D" ahead of the {d[timeL]}th month. In this simulation, we assume it to be [yellow][i]settled on the {d[timeL]}th month[/][/]. "D" = 45500.00 BUSD - total technology fee that has already been paid to RSR. If the resulting "D" is negative in value, EonLabs do not need to pay extra. After "D" is settled, EonLabs can start using Blade software on their own. From then on, EonLabs do not need to profit share with RSR on new strategies. RSR still continues to trade the existent funded sub-accounts (FSAs). RSR continues to receive RSR TECHNO FEE for the rest of the agreement period.
[#00FF00][b]RSR ACCRUED FEE[/][/] - Cumulative fee that the researcher (RSR) has received from EonLabs. It includes both the RSR TECHNO FEE and RSR BLADE REDUCED LICENSE FEE.

[#FFB6C1][b]EONLABS INJECTED FUND[/][/] ("Y%" of of the post-fee balance)
EonLabs recognizes RSR's performance by raising the funded sub-account (FSA) balance. As a monthly routine, EonLabs injects additional funds to the FSAs. Funding amount is "Y%" of the post-fee FSA balance total at the time. EonLabs injects funds monthly as long as WBSUP is maintained. It is the researcher's responsibility to maintain WBSUP. Funds injection stops once EonLabs obtains its own Blade software license.
[#FFB6C1][b]EONLABS ACCRUED INJECTED FUND[/][/] - Cumulative funds that EonLabs contributed to the funded sub-accounts (FSAs). It includes both the startup fund and the subsequent routinely injected fund.

[#BB8FCE][b]SETTLED EQUITY BALANCE MONTH END[/][/] - The total asset values of all funded sub-accounts (FSAs) at the end of the month. It is after all the fees payable to RSR and funds contributed by EonLabs.