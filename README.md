
# Fund Sub-Account (FSA) Partnership Simulation

`fsa_simulation.py` simulate a **funded sub-account (FSA) partnership** between EonLabs and Researcher (RSR). A worst-but-still-unfailing performance (**WBSUP**) is always assumed in all FSAs. **WBSUP** is perhaps the most important concept to consider. So please don't hesitate to contact EonLabs for more information if you have any questions.

- `fsa_simulation.py` will generate a table with ten (10) columns and twenty-five (25) rows. Each row represents a single month, from the 0th to the 24th. Each column's significance is detailed in [What Each Column Means](#what-each-column-means)
- They comprise information such as initial and subsequent fund injections, starting and ending balances of every month, realized profit, and settled RSR payment.
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