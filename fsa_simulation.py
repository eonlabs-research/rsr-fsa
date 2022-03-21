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
    table.add_column(f'[#00FF00]RSR REDUCED ONE- TIME FEE[/]', justify="right", width=7)
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
            sum(rsrLs)==0.00 #^ return zero if RSR ONE-TIME FEE has been paid
            and rsrAs[kM]<licnZ #^ return zero if RSR accrued fee has exceed ONE-TIME FEE
            #and eqbSs[kM]*rateR*rateS<licnZ #^ return zero if equity balance month start amount can potentially make up for the ONE-TIME FEE in its next extended asset value cycle
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
    d["scapX"]  = [i * 1000 for i in [float(x) for x in Prompt.ask('Startup trading capital injection to funded sub-account (FSA)? [green]\"X\"[/] (in thousand BUSD)', default='26 260').split()]]
    d["freqM"]  = IntPrompt.ask(f'Number of month for asset value to stagnate before extending beyond its last all-time high? [green]\"M\"[/]', default=2)
    d["rateR"]  = FloatPrompt.ask(f'Percentage of [#BB8FCE]SETTLED EQUITY BALANCE MONTH END[/] of {d["freqM"]}-month ago as [b][red]EXTENDED ASSET VALUE (EAV)[/][/]? [green]\"R%\"[/]', default=0.10)
    d["rateS"]  = FloatPrompt.ask(f'Percentage of [b][red]EXTENDED ASSET VALUE (EAV)[/][/] as [#00FF00]RSR TECHNO FEE[/] payable to RSR? [green]\"S%\"[/]', default=0.25)
    d["rateY"]  = FloatPrompt.ask(f'Percentage of the post-[#00FF00]RSR TECHNO FEE[/] FSA balance as [#FFB6C1]EONLABS INJECTED FUND[/] to FSA? [green]\"Y%\"[/]', default=0.30)
    d["licnZ"]  = FloatPrompt.ask(f'[#00FF00]RSR ONE-TIME FEE[/] amount as IP rights or sign-on bonus? (in BUSD) [green]\"$Z\"[/]', default=45500.00)
    d["timeL"]  = IntPrompt.ask(f'Max. # of months that EonLabs can wait to choose to settle the [#00FF00]RSR ONE-TIME FEE[/]? [green]\"L\"[/]', default=12)
    d["timeT"]  = d["freqM"] * 30 # day
    
    for x_startupCapital in d["scapX"]:
        d["x_startupCapital"] = x_startupCapital
        table,eqbSs,exAVs,rsrTs,rsrLs,rsrAs,eonFs,eqbEs = researcherPartnershipSimulationInTable(
        d["rateR"],d["rateS"],d["rateY"],d["x_startupCapital"],d["licnZ"],d["timeL"], Markdown(f'''# SIMULATION OF 24 MONTH WITH STARTUP CAPITAL OF {rd(x_startupCapital)} BUSD''')
        )
        textParameters      = (
            f'"X": [#00ffff]{rd(x_startupCapital)} BUSD[/] is the first [#FFB6C1]EONLABS INJECTED FUND[/] to the FSAs owned by EonLabs but managed by RSR',
            f'"-R%": [#00ffff]-{d["rateR"]*100}%[/] is the maximum allowed drawdown from any all-time highs (ATHs) on the equity curve (EC)',
            f'"M": [#00ffff]{d["freqM"]*30} days[/] is the maximum allowed stagnation of [b][red]EXTENDED ASSET VALUE (EAV)[/][/] from any ATHs on EC',
            f'"R%": [#00ffff]{d["rateR"]*100}%[/] is the rate of [b][red]EAV[/][/] from the monthly settled all-time highs every {d["freqM"]} months',
            f'"S%": [#00ffff]{d["rateS"]*100}%[/] of [b][red]EAV[/][/] ([#ffff00][i]above[/][/] [#BB8FCE]SETTLED EQUITY BALANCE MONTH END[/] of {d["freqM"]}-month ago) is payable to RSR',
            f'"Y%": [#00ffff]{d["rateY"]*100}%[/] of the equity balance ([#ffff00][i]after[/][/] [#00FF00]RSR TECHNO FEE[/] deducted) is the new funds injection',
            f'"Z": [#00ffff]{d["licnZ"]} BUSD[/] is [#00FF00]RSR ONE-TIME FEE[/] payable through [#00FF00]RSR ACCRUED TECHNO FEE[/] + [#00FF00]RSR REDUCED ONE-TIME FEE[/]',
            f'"L": [#00ffff]{d["timeL"]}-month[/] is the maximum wait time that EonLabs can choose to settle [#00FF00]RSR ONE-TIME FEE[/]',
        )
        textOneTimeFee      = (
            f'On the [#00ffff]{eonFs.index(0)}th month[/], [#FFB6C1]EONLABS INJECTED FUND[/] to the funded sub-accounts (FSAs) managed by the researcher (RSR) [#ffff00][i]stopped[/][/] because [#00FF00]RSR ACCRUED FEE[/] of [#00ffff]{rd(rsrAs[eonFs.index(0)])} BUSD[/] is [yellow][i]equal (or exceeded)[/][/] [#00ffff]{rd(d["licnZ"])} BUSD[/] ([#00FF00]RSR ONE-TIME FEE[/] "$Z"). And from this point forward:', 
            f'1. EonLabs is no longer obligated to inject/contribute more fund to the FSAs.',
            f'2. RSR grants EonLabs the rights of using predetermined intellectual properties so that EonLabs can use and operate them to generate trading strategies for the next twelve (12) months and to trade clients funds without having the need to profit share with RSR; or instead of granting the right to predetermined intellectual properties, RSR can join EonLabs as full-time employee.',
            f'3. Because the partnership contract period is two (2) years, RSR is responsible to continue to trade the FSAs that have been existent for the first {p.number_to_words(eonFs.index(0))} ({eonFs.index(0)}) months and is entitled to receive profit sharing from the FSAs for the remaining {p.number_to_words(24-eonFs.index(0))} ({24-eonFs.index(0)}) months.'
        )
        textSummary         = (
            f'[#00ffff]{rd(sum(rsrTs))} BUSD[/] or [#00ffff]{rdf(sum(rsrTs))} BUSD[/] is cumulative fee payable to the researcher (RSR).',
            f'[#00ffff]{rd(sum(eonFs))} BUSD[/] or [#00ffff]{rdf(sum(eonFs))} BUSD[/] is cumulative fund contributed by EonLabs.',
            f'[#00ffff]{rd(eqbEs[-1])} BUSD[/] or [#00ffff]{rdf(eqbEs[-1])} BUSD[/] is asset value of all FSAs belongs to EonLabs.',
            f'[#00ffff]{rd((eqbEs[-1]/sum(eonFs)-1)*100)}%[/] is the return on investment enjoyed by EonLabs based on [#FFB6C1]EONLABS ACCRUED INJECTED FUND[/].'
        )
        console.print(
            table,
            Markdown(f"""#  PARAMETERS: {rdf(x_startupCapital)} BUSD AS STARTUP CAPITAL  """), *textParameters,
            Markdown(f"""#  FULL USAGE RIGHT OF IPs / FULL-TIME EMPLOYMENT OF RSR {eonFs.index(0)}th MONTH  """), *textOneTimeFee,
            Markdown(f"""#  SUMMARY AT THE END OF THE 24TH MONTH  """), *textSummary,
            sep= "\n")
        console.print(Markdown(""" ---------- """))
        console.print(Markdown(""" ---------- """))
    stopScript  = bool(console.input(f'\n[#FF4500]{"v"*106}[/]\nEnter nothing to run this script again. Enter something to stop this script: \n[#FF4500]{"v"*106}[/]\n'))
    console.print(Markdown(""" -----------------------------  """))