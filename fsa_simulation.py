from traceback_with_variables import activate_by_import # for finding out why exception occurs
from rich.jupyter import print # pip install rich
from rich.prompt import Prompt, IntPrompt, FloatPrompt
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
console = Console()
from numerize import numerize # pip install numerize
import inflect
d = {}
p = inflect.engine()
rdf = lambda x: "{:.2f}".format(x)
rd = lambda x: numerize.numerize(x)
def textOverviewWrapper():
    txtOverview = f''''
    ''# EXPLAIN WHAT EACH COLUMN MEANS
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
    
    '''
def overviewPrint(filename, start, finish): #*  Print whatever that is between the "start" and "finish" strings
    with open(filename, "r", encoding="utf-8") as file:
        copy = False
        for line in file:
            if start in line:
                copy = True
                continue
            elif finish in line:
                copy = False
                continue
            elif copy:
                if "\'\'" in line and line.strip(): # print only when the line is not empty
                    console.print(Markdown(line.strip().lstrip("\'\'").format(d=d)))
                elif line.strip(): # print only when the line is not empty
                    console.print(line.strip().format(d=d))
def researcherPartnershipSimulationInTable(rateR,rateS,rateY,x_startupCapital,licnZ,timeL,tableTitle):
    eqbSs, exAVs, rsrTs, rsrTA, rsrLs, rsrAs = [0.00], [0.00], [0.00], [0.00], [0.00], [0.00]
    eonFs = [x_startupCapital]
    eqbEs = [eqbSs[0] + exAVs[0] - rsrTs[0] + eonFs[0]]
    table = Table(show_header=True, header_style="bold", title=tableTitle, title_style="bold underline magenta")
    table.add_column(r'[#BB8FCE]EQUITY BALANCE MONTH START[/]', justify="right", width=8)
    table.add_column(r'M', style="dim", width=3)
    table.add_column(f'[red]EXTENDED ASSET VALUE[/] [#00ffff]R%:{rdf(rateR)}[/]', justify="right", width=8)
    table.add_column(f'[#00FF00]RSR TECHNO FEE[/] [#00ffff]S%:{rdf(rateS)}[/]', justify="right", width=8)
    table.add_column(f'[#00FF00]RSR ACCRUED TECHNO FEE[/]', justify="right", width=8)
    table.add_column(f'[#00FF00]RSR BLADE REDUCED LICENSE FEE[/]', justify="right", width=7)
    table.add_column(f'[#00FF00]RSR ACCRUED FEE[/]', justify="right", width=8)
    table.add_column(f'[#FFB6C1]EONLABS INJECTED FUND[/] [#00ffff]Y%:{rdf(rateY)}[/]', justify="right", width=9)
    table.add_column(f'[#FFB6C1]EONLABS ACCRUED INJECTED FUND[/]', justify="right", width=8)
    table.add_column(r'[#BB8FCE]SETTLED EQUITY BALANCE MONTH END[/]', justify="right", width=8)
    table.add_row(f'{rd(eqbSs[0])}', f'{0}',f'{rd(exAVs[0])}',f'{rd(rsrTs[0])}',f'{rd(rsrTA[0])}',f'{rd(rsrLs[0])}',f'{rd(rsrAs[0])}',f'{rd(eonFs[0])}',f'{rd(sum(eonFs))}',f'{rd(eqbEs[0])}',)
    for kM in range(1,25):
        eqbSs.append(eqbEs[(kM-1)])
        exAVs.append(eqbSs[kM]*rateR if kM % d["freqM"] == 0 else 0.00)
        rsrTs.append(exAVs[kM]*rateS)
        rsrTA.append(sum(rsrTs))
        rsrLs.append(licnZ-sum(rsrTs) if (licnZ-sum(rsrTs) if kM == timeL else 0.00) > 0.00 else 0.00)
        rsrAs.append(sum(rsrTs) + sum(rsrLs))
        eonFs.append((eqbSs[kM] + exAVs[kM] - rsrTs[kM])*d["rateY"] if (
            sum(rsrLs)==0.00 #^ return zero if RSR license fee has been paid
            and rsrAs[kM]<licnZ #^ return zero if RSR accrued fee has exceed software license fee
            #and eqbSs[kM]*rateR*rateS<licnZ #^ return zero if equity balance month start amount can potentially make up for the license fee in its next extended asset value cycle
            )  else 0.00)
        eqbEs.append(eqbSs[kM] + exAVs[kM] - rsrTs[kM] + eonFs[kM])
        table.add_row(f'{rd(eqbSs[kM])}',
                      f'[b][yellow]{kM}[/][b]' if eonFs[kM] == 0 else f'{kM}',
                      f'{rd(exAVs[kM])}',f'{rd(rsrTs[kM])}',f'{rd(rsrTA[kM])}',f'{rd(rsrLs[kM])}',f'{rd(rsrAs[kM])}',
                      f'[b][yellow]{rd(eonFs[kM])}[/][/]' if eonFs[kM] == 0 else f'{rd(eonFs[kM])}',
                      f'{rd(sum(eonFs))}',f'{rd(eqbEs[kM])}',)
    return table,eqbSs,exAVs,rsrTs,rsrLs,rsrAs,eonFs,eqbEs
stopScript = False
while not(stopScript):
    console.print(Markdown(""" -------------------------------------------------------------------------  """))
    d["scapX"]  = [i * 1000 for i in [float(x) for x in Prompt.ask('Startup trading capital injection? [green]\"X\"[/] (in thousands)', default='26 260').split()]]
    d["rateR"]  = FloatPrompt.ask(f'Rate of extended asset value? [green]\"R%\"[/]', default=0.10)
    d["freqM"]  = IntPrompt.ask(f'Stagnation of EAV, i.e. Month needed to extend assset {d["rateR"]*100}% beyond the last all-time high? [green]\"M\"[/]', default=2)
    d["rateS"]  = FloatPrompt.ask(f'Percentage of profit share on the extended asset value? [green]\"S%\"[/]', default=0.25)
    d["rateY"]  = FloatPrompt.ask(f'Injected fund amount as a percentage of the post-fee sub-account balance? [green]\"Y%\"[/]', default=0.30)
    d["licnZ"]  = FloatPrompt.ask(f'Software license fee amount? [green]\"$Z\"[/]', default=45500.00)
    d["timeL"]  = IntPrompt.ask(f'Max. # of months that [#00FF00]RSR BLADE REDUCED LICENSE FEE[/] can be settled? [green]\"L\"[/]', default=12)
    d["timeT"]  = d["freqM"] * 30 # day
    overviewPrint('fsa_simulation.py', "\'\'\'\'", "\'\'\'")
    for x_startupCapital in d["scapX"]:
        d["x_startupCapital"] = x_startupCapital
        textParameters      = (
            f'"X": [#00ffff]{rd(x_startupCapital)} BUSD[/] is the first [#FFB6C1]EONLABS INJECTED FUND[/] to the FSAs owned by EonLabs but managed by RSR',
            f'"-R%": [#00ffff]-{d["rateR"]*100}%[/] is the maximum allowed drawdown from any all-time high on equity curve',
            f'"R%": [#00ffff]{d["rateR"]*100}%[/] is the rate of [b][red]EXTENDED ASSET VALUE[/][/] every {d["freqM"]} months, simulating the WBSUP',
            f'"S%": [#00ffff]{d["rateS"]*100}%[/] of the extended asset value ([#ffff00][i]above[/][/] last ATH marked on settlement date) is payable to RSR',
            f'"Y%": [#00ffff]{d["rateY"]*100}%[/] of the equity balance （[#ffff00][i]after[/][/] [#00FF00]RSR TECHNO FEE[/] deducted) as new funds injection',
            f'"Z": [#00ffff]{d["licnZ"]}[/] license fee/year payable through [#00FF00]RSR ACCRUED TECHNO FEE[/] + [#00FF00]RSR BLADE REDUCED LICENSE FEE[/]',
            f'"L": [#00ffff]{d["timeL"]}[/] is the maximum number of month that EonLabs can settle the difference of software license',
        )
        table,eqbSs,exAVs,rsrTs,rsrLs,rsrAs,eonFs,eqbEs = researcherPartnershipSimulationInTable(
        d["rateR"],d["rateS"],d["rateY"],d["x_startupCapital"],d["licnZ"],d["timeL"], Markdown(f'''# SIMULATION OF 24 MONTH WITH STARTUP CAPITAL OF {rd(x_startupCapital)} BUSD''')
        )
        textLicenseFee      = (
            f'On the [#00ffff]{eonFs.index(0)}th month[/], [#FFB6C1]EONLABS INJECTED FUND[/] to the funded sub-accounts (FSAs) managed by the researcher (RSR) [#ffff00][i]stopped[/][/] because [#00FF00]RSR ACCRUED FEE[/] of [#00ffff]{rd(rsrAs[eonFs.index(0)])} BUSD[/] is [yellow][i]equal (or exceeded)[/][/] [#00ffff]{rd(d["licnZ"])} BUSD[/] (SOFTWARE LICENSE FEE "$Z"). And from this point forward:', 
            f'1. EonLabs is no longer obligated to inject/contribute more fund to the FSAs from this month forward.',
            f'2. RSR grants EonLabs the Blade software license so that EonLabs can use and operate it to generate trading strategies for the next twelve (12) months and to trade clients funds without having the need to profit share with RSR.',
            f'3. Because the partnership contract period is two (2) years, RSR is responsible to continue to trade the FSAs that have been existent for the first {p.number_to_words(eonFs.index(0))} ({eonFs.index(0)}) months and is entitled to receive profit sharing from the FSAs for the remaining {p.number_to_words(24-eonFs.index(0))} ({24-eonFs.index(0)}) months.'
        )
        textSummary         = (
            f'[#00ffff]{rd(sum(rsrTs))} BUSD[/] or [#00ffff]{rdf(sum(rsrTs))} BUSD[/] is cumulative fee payable to the researcher (RSR).',
            f'[#00ffff]{rd(sum(eonFs))} BUSD[/] or [#00ffff]{rdf(sum(eonFs))} BUSD[/] is cumulative fund contributed by EonLabs.',
            f'[#00ffff]{rd(eqbEs[-1])} BUSD[/] or [#00ffff]{rdf(eqbEs[-1])} BUSD[/] is asset value of all FSAs belongs to EonLabs.',
            f'[#00ffff]{rd((eqbEs[-1]/sum(eonFs)-1)*100)}%[/] is the return on investment enjoyed by EonLabs based on [#FFB6C1]EONLABS ACCRUED INJECTED FUND[/].'
        )
        console.print(
            Markdown(f"""#  PARAMETERS: {rdf(x_startupCapital)} BUSD AS STARTUP CAPITAL  """), *textParameters,
            table,
            Markdown(f"""#  FULL USAGE RIGHT OF THE BLADE SOFTWARE ON THE {eonFs.index(0)}th MONTH  """), *textLicenseFee,
            Markdown(f"""#  SUMMARY AT THE END OF THE 24TH MONTH  """), *textSummary,
            sep= "\n")
    stopScript  = bool(console.input(f'\n[#FF4500]{"v"*106}[/]\nEnter nothing to run this script again. Enter something to stop this script: \n[#FF4500]{"v"*106}[/]\n'))
    console.print(Markdown(""" -----------------------------  """))