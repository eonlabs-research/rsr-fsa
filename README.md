
# Researcher (RSR) Funded Sub-Account (FSA) Partnership Simulation

`fsa simulation.py` simulates an EonLabs-Researcher **funded sub-account (FSA) partnership** (RSR). In all FSAs, a worst-but-still-unfailing performance (**WBSUP**) is assumed. The most important concept to consider is **WBSUP**. So, if you have any questions, please don't hesitate to contact EonLabs for more information.

## FEATURES DESCRIPTION

- The script `fsa simulation.py` creates a table with ten (10) columns and twenty-five (25) rows. It simulates a standard 24-month contract period from the 1st to the 25th, each row represents a single month. The 0-th month is shown as a startup line.
- The columns include data on initial and subsequent fund injections, monthly beginning and ending balances, realized profit, and settled RSR payment.
- There is no expectation of loss. Profit is the only thing that is simulated.
- Extended asset value (EAV) stagnation is always less than two (2) months.
- You have the option of changing the duration of the stagnation, which can be 1 or 2 months. EonLabs will not accept anything longer than a two-month period because it would fail the WBSUP's minimum requirements (i.e. exceed the risk tolerance as defined by WPSUP).
- The terms `L-th month`, `D`, and `Z` refer to a one-time fee to pay for predetermined intellectual properties (e.g. software algorithms) or a sign-on bonus (in the case of full-time employment) that can be built into the simulation.

The default parameter settings for `fsa simulation.py` are not set in stone. Researchers (RSR) are encouraged to play around with the parameters until they find a set of settings that they can submit to EonLabs for consideration.

## PREREQUISITES

Install the dependency packages: `pip install --upgrade pip traceback_with_variables rich numerize inflect`

## WORST-BUT-STILL-UNFAILING PERFORMANCE (WBSUP)

**WBSUP** is a standard that EonLabs use to assess the RSR's trading performance. It is designed in such a way that everyone knows what to expect before trading begins.

### DEFINITION OF WBSUP

**WBSUP** denotes that a _minimal_ **EXTENDED ASSET VALUE (EAV)** must be obtained within a specified time period, `"T"` (e.g. `60 days` or `1 month`). It's worth noting that the `EAV` value is dynamically calculated and proportional to the recent downside risk taken. RSR is only allowed to take a maximum of `-R%` of risk on the downside.

#### MAXIMUM ALLOWED DOWNSIDE RISK FROM ALL-TIME HIGH (A)

If `"-R%"` = `-10%` (i.e. `-0.10`), the maximum drawdown from _any_ all-time high on the equity curve of total asset value cannot be greater than the multiple of `0.10`.

##### As an illustration

Let's say point A (`"A"`) on the equity curve is an all-time high. The maximum drawdown between `"A"` and before `"A"` is surpassed again is measured in `"-R%"`. During drawdown, `"-R%"` cannot exceed an agreed-upon value (e.g. `-0.10`). WBSUP is considered a failure if `"-R%"` exceeds the agreed-upon value.

### THE LAST TIME ALLOWED TO REACH THE NEXT ALL-TIME HIGH (B)

Let's continue with the previous example. Let's pretend that point B (`"B"`) is the next all-time high on the equity curve, and that `"B"="A"*(1+"R%")`. The recent drawdown `"-R%"`, which occurs between `"A"` and `"B"`, is equal to the value of `"R%"` in the equation. Every drawdown from the peaks appears to be unique, and as long as they do not exceed the maximum allowed downside risk from their respective `"A"`s, the actual `"-R%"` values may differ from one to the next. The equity curve must reach `"B"` within a certain agreed-upon period (`"T"`) according to WBSUP. WBSUP is considered a failure if `"B"` is not achieved within that time frame.

#### To give you an example

Let's say EonLabs and RSR agree on `"T"` to be `60 days`. If the equity curve has fallen 5.8% (or `-0.058`) from its all-time high (`"A" = 48390 BUSD`), it has reached a trough (`80000*(1-0.058) = 75360 BUSD`).
WBSUP mandates that a _minimal_ **EXTENDED ASSET VALUE (EAV)** (i.e. `"A"*"R%" = 80000*0.058 = 4640 BUSD`) be achieved within `60 days` of the day `"A"` occurs. In other words, within `60 days` of the day `"A"` occurs, the equity balance of total asset value must equal or exceed `"B"` (i.e. `"A" * (1+"R%") = 80000 * (1+0.058) = 84640 BUSD`).

## EXPLAIN THE MEANING OF EACH COLUMN

### MONTHLY EQUITY BALANCE START (X)

- The Researcher (RSR) is in charge of trading a predetermined number of funded sub-accounts (FSAs). The asset value of all FSAs at the start of the month is `"X"`.
- `"X"` is a stablecoin denominator (e.g. BUSD).
- RSR has complete control over the funds in the FSAs and can rebalance them at any time.

### EXTENDED ASSET VALUE (EAV = A * R%)

- `EAV` simply means the money profited from trading the sub-accounts.
- Here we simulate `"R%"` as a fixed value that is reached every `"M"` months. 
- EonLabs captures Binance's Margin Balance hourly during LIVE trading. Profit and loss figures, both realized and unrealized, are included in the data (PnL). Only profit that has been realized is counted toward `"A"` and `"B"`. However, unrealized losses will be counted toward the `"-R%"` drawdown. As a result, it's critical for an RSR to size each trading position carefully so that the sum of all losses (including unrealized ones) in all the funded sub-accounts (FSA) that the RSR manages since the most recent all-time high asset value (`"A"`) does not exceed the multiple of `"R%"` and `"A"`.

### RSR TECHNO FEE (A * R * S%)

- The multiple of **EXTENDED ASSET VALUE** (`EAV`) and `"S%"` is **RSR TECHNO FEE**.
- It is paid to RSR on a monthly basis by EonLabs as long as WBSUP is maintained by RSR.
- WBSUP is evaluated solely on the basis of interim profit and loss (realized and unrealized).
- The **RSR TECHNO FEE**, which is calculated on the month-end settlement date only, will not be calculated using interim P&L.

### TECHNO FEE ACCRUED BY RSR

Cumulative **RSR TECHNO FEE** that RSR received from EonLabs.

### RSR REDUCED ONE-TIME FEE (D)

- The difference between the **ONE-TIME FEE** (`"Z" BUSD`) and the **RSR ACCRUED FEE** is referred to as `"D"`.
- It is a one-time fee that EonLabs must pay to RSR by the end of a specific month (e.g. 12th month).
- EonLabs, on the other hand, has the right to settle the `"D"` payment ahead of the time.
- Here we assume `"D"` is settled on the `L-th month`.
- `"D" = "Z" BUSD - RSR ACCRUED TECHNO FEE`, where "Z" represents the **ONE-TIME FEE**.
- EonLabs does not have to pay anything extra if the resulting `"D"` is negative in value.
- EonLabs can begin using RSR's predetermined intellectual properties on their own once `"D"` is resolved. EonLabs will no longer be required to profit share with RSR if the profit derived from the newly generated strategies.
- RSR is still trading the existing funded sub-accounts (FSAs). For the remainder of the agreement period, RSR will continue to receive RSR TECHNO FEE.

### ACCRUED RSR FEE

Cumulative fee that the researcher (RSR) has received from EonLabs. Both **RSR TECHNO FEE** and **RSR REDUCED ONE-TIME FEE** are included.

### FUND INJECTED BY EONLABS (Y percent of of the post-fee balance)

- RSR's trading performance is recognized by EonLabs by an increase in the funded sub-account (FSA) balance.
- EonLabs injects additional funds into the FSAs on a monthly basis.
- The funding amount is equal to "Y%" of the total post-fee FSA balance at the time.
- It is the researcher's responsibility to maintain WBSUP.
- As long as WBSUP is maintained, EonLabs injects funds on a monthly basis.
- Whenever RSR's total receivable equals or exceeds **ONE-TIME FEE**, EonLabs may choose to stop further funds injection.

### EONLABS ACCRUED INJECTED FUND

EonLabs' cumulative contributions to the funded sub-accounts (FSAs). It includes the initial startup fund as well as the subsequent regularly injected fund.

### MONTH END EQUITY BALANCE SETTLED

At the end of the month, the total asset values of all funded sub-accounts (FSAs) are totaled. It is the result of a post-balance of RSR fees and funds contributed by EonLabs.
