
# Fund Sub-Account (FSA) Partnership Simulation

`fsa_simulation.py` simulate a **funded sub-account (FSA) partnership** between EonLabs and Researcher (RSR). A worst-but-still-unfailing performance (**WBSUP**) is always assumed in all FSAs. **WBSUP** is perhaps the most important concept to consider. So please don't hesitate to contact EonLabs for more information if you have any questions.

- `fsa_simulation.py` will generate a table with ten (10) columns and twenty-five (25) rows. Each row represents a single month, from the 0th to the 24th.
- The columns comprise information such as initial and subsequent fund injections, starting and ending balances of every month, realized profit, and settled RSR payment.
- Not loss is assumed. Only profit is simulated.
- Stagnation of extended asset value (EAV) is always less than two (2) months.
- You can choose to adjust the stagnation，which is either 1 or 2 month. Anything longer than a two-month period is not acceptable by EonLabs since it would fail the minimal requirements of WBSUP (i.e. exceed the risk tolerance as defined by WPSUP).

`fsa_simulation.py` default parameter settings are not fixed in stone. Researchers (RSR) are urged to experiment with the parameters until they discover an appropriate set of settings to submit to EonLabs for consideration.

# WORST-BUT-STILL-UNFAILING PERFORMANCE (WBSUP)

**WBSUP** is used to evaluate the trading performance of researchers (RSR). It is built in such a manner that everyone understands what is anticipated before trading starts.

## DEFINITION OF WBSUP

**WBSUP** means that a _minimal_ **EXTENDED ASSET VALUE (EAV)**, "R%" (e.g. 10% or 0.10), must be gained within an agreed period of time, "T" (e.g. 60 days or 1 month). Note that the value of "R%" is evaluated dynamically and is relative to the downside risk taken recently. The maximum allowed downside risk to be taken by RSR is "-R%"

### MAXIMUM ALLOWED DOWNSIDE RISK FROM ALL-TIME HIGH ("A")

If "-R%" = -10% (or `-0.10`), it means that the maximum drawdown cannot be larger than the multiple of `0.10` from _any_ all-time high on the equity curve of total asset value.

#### FOR EXAMPLE

Let's say point A ("A") is an all-time high on equity curve. "-R%" is the extent of maximum drawdown between "A" and before "A" is surpassed again. "-R%" cannot exceed an agreed value (e.g. `-0.10`) during drawdown. If "-R%" exceeded the agreed value, WBSUP is considered failed.

### MAXIMUM ALLOWED TIME TO REACH NEXT ALL-TIME HIGH ("B")

Let's continue from the example above. Let's say point B ("B") is the next all-time high on equity curve, where `"B"="A"*(1+"R%")`. The value of "R%" in the equation equals the recent drawdown "-R%", which happens between "A" and "B". Apparently, every drawdown from the peaks is different and as long as they do not exceed the maximum allowed downside risk from their respective "A"s, the actual "-R%" values might vary from one to another. WBSUP requires that the equity curve must attain "B" within certain agreed period ("T"). If "B" cannot be attained within that period, WBSUP is considered failed.

#### FOR EXAMPLE

To illustrate, let's say "T" is agreed by EonLabs and RSR to be `60 days`. If there is a 5.8% (or `-0.058`) drawdown from an all-time high (`"A" = 48390 BUSD`), it means the equity curve is hitting a trough (`80000*(1-0.058) = 75360 BUSD`).
WBSUP requires that a _minimal_ **EXTENDED ASSET VALUE (EAV)** (`"A"*"R%" = 80000*0.058 = 4640 BUSD`) must be gained within `60 days` after the day when "A" happens. In other words, the equity balance of total asset value must attain or exceed "B" (`"A" * (1+"R%") = 80000 * (1+0.058) = 84640 BUSD`) within `60 days` after the day when "A" happens.

# EXPLAIN WHAT EACH COLUMN MEANS

### EQUITY BALANCE MONTH START (X)

The Researcher (RSR) is responsible for trading an agreed number of funded sub-accounts (FSAs). `"X"` is the asset value of all FSAs at the beginning of the month. `"X"` is denominated in stablecoin (e.g. BUSD). RSR can freely rebalance the funds among the FSAs at any time.

### EXTENDED ASSET VALUE (A * R%)

It means trading profit. Here we simulate `"R%"` as a fixed value that is attained every `"M"` months. During LIVE trading, EonLabs capture Margin Balance hourly from Binance. The captured data includes realized and unrealized profit and loss (PnL). Only realized profit is counted towards `"A"` & `"B"`. But momentary unrealized losses will be counted toward drawdown of `"-R%"`. Therefore it is important for an RSR to size each trading position carefully so that the sum of all losses _including unrealized ones_) -- since the most recent all-time high asset value (`"A"`) in all the funded sub-accounts (FSA) that the RSR manages -- does not exceed the the multiple of `"R%"` and `"A"`.

### RSR TECHNO FEE (A * R% * S%)

RSR TECHNO FEE is the multiple of EXTENDED ASSET VALUE (`"A"*"R%"`) and `"S%"`. It is payable monthly by EonLabs to RSR as long as WBSUP is maintained by RSR. Interim profit and loss (realized & unrealized) is monitored to assess WBSUP only. Interim P&L will not be used to calculate **RSR TECHNO FEE**, which is calculated on the month-end settlement date only.

### RSR ACCRUED TECHNO FEE

Cumulative **RSR TECHNO FEE** that RSR received from EonLabs.

### RSR REDUCED LICENSE FEE (D)

`"D"` is the difference between the license fee (`"Z" BUSD`) and **RSR ACCRUED FEE**. It is a one-time fee payable by EonLabs to RSR not later than certain month (e.g. 12th month). However, EonLabs is entitled to settle the payment of `"D"` ahead of it. In this simulation, we assume it to be settled on the `L-th month`. 

`"D" = "Z" BUSD - RSR ACCRUED TECHNO FEE`, where `"Z"` is the license fee.  

If the resulting `"D"` is negative in value, EonLabs do not need to pay anything extra. After `"D"` is settled, EonLabs can start using RSR's system software on their own. From then on, EonLabs do not need to profit share with RSR on new strategies. RSR still continues to trade the existent funded sub-accounts (FSAs). RSR continues to receive RSR TECHNO FEE for the rest of the agreement period.

### RSR ACCRUED FEE

Cumulative fee that the researcher (RSR) has received from EonLabs. It includes both the **RSR TECHNO FEE** and **RSR REDUCED LICENSE FEE**.

### EONLABS INJECTED FUND (Y% of of the post-fee balance)

EonLabs recognizes RSR's performance by raising the funded sub-account (FSA) balance. As a monthly routine, EonLabs injects additional funds to the FSAs. Funding amount is `"Y%"` of the post-fee FSA balance total at the time. EonLabs injects funds monthly as long as WBSUP is maintained. It is the researcher's responsibility to maintain WBSUP. Funds injection stops once EonLabs obtains RSR's system software license.

### EONLABS ACCRUED INJECTED FUND

Cumulative funds that EonLabs contributed to the funded sub-accounts (FSAs). It includes both the startup fund and the subsequent routinely injected fund.

### SETTLED EQUITY BALANCE MONTH END

The total asset values of all funded sub-accounts (FSAs) at the end of the month. It is after all the fees payable to RSR and funds contributed by EonLabs.