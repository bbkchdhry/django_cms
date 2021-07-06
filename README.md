## Overview of RealRate Codeflow

- RealRate-Private
	- [Main Executable File: run.py](#run.py)
	- main.py
		- [evaluate_model(args)](#evaluate_model)
		- [causing_years(args, model, year, args.cluster, output_path)](#causing_years)
	- industry
		- de_life (model.py)
			- [model(pa_year)](#de_life_model) # ToDo
		- de_disability (model.py)
			- [model(pa_year)](#de_disability_model) # ToDo
	- [Understanding graphs.json](#graph) # ToDo


#### run.py


1. Calls function `make_parser()` -> returns ArgumentParser

		In subcommands/subparser a function is set while calling a specific subcommands.

		subcommands		function
		-------------------------------------------------------------------
		evaluate		main.evaluate_model (evaluate_model in main.py)
		plot			main.plot	(plot method in main.py)
		snail_mail		main.snail_mail	(snail_mail method in main.py)
		send_email		main.send_mail	(send_mail method in main.py) 

		optional arguments:
			-h, --help			show this help message and exit
			--industry 			{de_life,de_disability,generic}
			                    The industry model used to rate the companies (default: de_life)
			--cluster CLUSTER	The group of companies inside the industry which 
								should be rated. (default: None)
			--years YEARS		List of years to generate output for 
								(use python list syntax) (default: [2018])

		subcommands:
			{evaluate,plot,snail-mail,send-email,report-svg}
		    evaluate            Evaluate model and create graphs.json. 
		    					Required to be run before other commands
		    plot                Render images for the generated graphs.
		    snail-mail          Generate PDFs to print and send via snail mail.
		    send-email          Send e-mails to companies with good rating. 
		    					You will be asked for confirmation before sending.
		    report-svg          Generate a single-sheet report in an SVG file

2. Get all of the arguments set in `make_parser()` using parser.parse_args()

	   	Namespace(
	   		cluster=None, 
	   		estimate=False, 
	   		func=<function evaluate_model at 0x7f424b12b550>, 
	   		industry='de_life', 
	   		simulate=False, 
	   		subcommand='evaluate', 
	   		years=[2018]
	   	)

3. Calls `load_settings` of config.py -> returns module of (model, mailing, emailing)

		module		function
		----------------------
		model 		industry.{industry}.model [{industry} is replaced by arg industry value]
		mailing 	industry.{industry}.mailing.mailing
		emailing	industry.{industry}.emailing.emailing

4. Set default cluster if not explicitly specified.

		CLUSTERS = {
		    # first one is default
		    "pure_life": "Lebensversicherer",
		    "risk_life": "Risikoversicherer",
		}

		This constant is set in 'industry.{industry}.model' module. 
		Converts CLUSTERS to list to get the keys 'pure_life' and 'risk_life', args.cluster 
		is set to pure_life if no cluster is passed.

5. Finally the function set in subpraser `(Setp 1)` is called.

		For example,
			./run.py evaluate (Calls main.evaluate_model from main.py with the arguments)

---
<p align="right">[Back to Top]()</p>

#### evaluate_model
`Arguments: (args)`

1. `load_settings(args)` is called to get the module `industry.{industry}.model`.

2. Generate an output path using industry and cluster

		output_path_all_years = Path("output", args.industry, args.cluster)
		output_path_all_years = 'output/de_life/pure_life'

3. Iterate over the years passed in args, by default only '2018' year is passed.
	*	Generate an output path for specific year.

			output_path = output_path_all_years / str(year)

	*	Create a directory of the output_path if not created.
	
	*	Call `causing_years(args, model, year, args.cluster, output_path)` method from 
		the same main.py file.
	
	*	Store the result of `causing_years` method in analyze_years dict.

			analyze_years[year] = result_from_causing_years_method
	
	*	Fetch graph_dat from the result of `causing_years` method.

			graphs = analyze_years[year]["graph_dat"]
    
    *	Assign cluster in cluster_label key in graphs.

    		graphs["cluster_label"] = model.CLUSTERS[args.cluster]
    
    *	Assign full names of nodes in nodes_full_name key in graphs.

    		graphs["nodes_full_name"] = 
    		analyze_years[year]["model_dat"]["nodes_full_name"]
    
    *	Round all the float values to 6 significant figures to make results stable 
    	even with minor floating point inaccuracies using `round_sig_recursive` from utils.py file.

        	graphs = utils.round_sig_recursive(graphs, sig=6)
    
    *	Finally, save all the graphs data in graphs.json file in asc order.

	        with open(output_path / "graphs.json", "w") as f:
	            json.dump(graphs, f, sort_keys=True, indent=4)

	*	At last, ranking_years method is called to show ranks and changes over years and
		save the result in 

		`output_path / logging.txt`

		Example:

			                          2019
			DL1001 AM                   55
			DL1005 Württ.               42
			DL1006 Allianz              35

---
<p align="right">[Back to Top]()</p>

#### causing_years
`Arguments: (args, model, year, args.cluster, output_path)`

Perform causing for all years

    load_dat: xdat, ymdat
    from load_dat but not in causing:
      year, company_ids, table_company, xvars_add, xdat_add # yyy
    from model.model but not in causing:
      base_var, rat_var, rel_var, x_basevars, y_basevars # yyy

1. Get PA_YEARS from industry model, `pa_year = model.PA_YEARS[year]`
	
		{
			"2018": {
			    "IRate": 0.00831,
			    "ISpread": 0.01,
			    "TaxRate": 0.25,
			    "deltaBasis": 0.06,
			    "MSLrel": 0.05,
			    "sigma": 0.04,
			    "Beteiligungsquote": 0.75
			}
		}

2. Calls `model` method of `industry.{industry}.model` module.
	
		model_dat = model.model(pa_year)

		Returned values:

		['alpha', 'base_var', 'define_equations', 'dir_path', 'dof', 'estimate_bias', 'final_var', 
		'nodes_full_name', 'rat_var', 'rel_var', 'show_nr_indiv', 'x_basevars', 'xvars', 'y_basevars', 
		'ymvars', 'ymvars_db', 'yvars']

3. Simulate or Load Data.

	*	If simulate is True then call `rr_simulate(model_dat, year)` method in main.py file, which returns the following.

			load_dat = rr_simulate(model_dat, year)

			Returned values:

			{
		        "xdat": xdat,
		        "ymdat": ymdat,
		        "year": year,  # not in causing
		        "company_ids": company_ids,  # not in causing
		        "table_company": table_company,  # not in causing
		        "xvars_add": xvars_add,  # not in causing
		        "xdat_add": xdat_add,  # not in causing
	    	}

	*	If simulate is False, which is by default, then call `load_db(pa_data, model_dat["xvars"], model_dat["yvars"], year)` from industry model.

			pa_data = 
				{
		            "cluster": cluster,
		            "country": model.COUNTRY,
		            "industry": args.industry,
	        	}

			load_dat = model.load_db(pa_data, model_dat["xvars"], model_dat["yvars"], year)

			Returned values:

			['company_ids', 'industry', 'table_company', 'xdat', 'xdat_add', 'xvars_add', 'year', 'ymdat']

	*	Update `model_dat` with `load_data`

			model_dat.update(load_data)

			Returned result:

			['alpha', 'base_var', 'company_ids', 'define_equations', 'dir_path', 'dof', 'estimate_bias', 
			'final_var', 'industry', 'nodes_full_name', 'rat_var', 'rel_var', 'show_nr_indiv', 'table_company',
			'x_basevars', 'xdat', 'xdat_add', 'xvars', 'xvars_add', 'y_basevars', 'year', 'ymdat', 'ymvars', 
			'ymvars_db', 'yvars']

	*	Update `analyze_year`; `analyze(model_dat, estimate=args.estimate)` method of 
		`causing` is called.

			analyze_year = {
		        "final_var": model_dat["final_var"],
		        "pa": pa_data,  # ToDo: does not depend on year
		    }

		    analyze_year["pa"].update(pa_year)  # add pa_year to analyze_dat

		    analyze_year.update(causing.analyze(model_dat, estimate=args.estimate))

		    	returns => ['estimate_dat', 'graph_dat', 'indiv_dat', 'model_dat']

		    After updating final returned result:

			['estimate_dat', 'final_var', 'graph_dat', 'indiv_dat', 'model_dat', 'pa']

	*	Add rank and final values to each company.

			final_var_idx = analyze_year["model_dat"]["yvars"].index(model_dat["final_var"])
		    final_vals = list(analyze_year["model_dat"]["yhat"][final_var_idx, :])
		    sorted_final_vals = sorted(final_vals, reverse=True)

		    for company, final_val in zip(
		        analyze_year["model_dat"]["table_company"], final_vals
		    ):
		        company["final_val"] = final_val
		        company["rank"] = sorted_final_vals.index(final_val) + 1

	*	Finally, return `analyze_year`.

			Final Returned result:

			estimate_dat: None

			final_var: ökEKQuote

			graph_dat:
			['base_var', 'company_ids', 'dir_path', 'direct_theo', 'edx', 'edy', 'ex_indivs', 'ex_theo', 'exj_indivs', 'exj_theo', 'ey_indivs', 'ey_theo', 'eyj_indivs', 'eyj_theo', 'eyx_indivs', 'eyx_theo', 'eyy_indivs', 'eyy_theo', 'fdx', 'fdy', 'idx', 'idy', 'is_all_graph', 'model_dat_condition', 'mx_indivs', 'mx_theo', 'my_indivs', 'my_theo', 'show_nr_indiv', 'table_company', 'xnodes', 'ynodes']
			
			indiv_dat:
			['dx_mat', 'dy_mat', 'ex_indivs', 'exj_indivs', 'ey_indivs', 'eyj_indivs', 'eyx_indivs', 'eyy_indivs', 'mx_indivs', 'my_indivs', 'xdat_based', 'yhat_based']

			model_dat:
			['alpha', 'base_var', 'company_ids', 'define_equations', 'dir_path', 'direct_theo', 'dof', 'edx', 'edy', 'estimate_bias', 'ex_theo', 'ex_theos', 'exj_theo', 'exj_theos', 'ey_theo', 'ey_theos', 'eyj_theo', 'eyj_theos', 'eyx_theo', 'eyx_theos', 'eyy_theo', 'eyy_theos', 'fdx', 'fdy', 'final_var', 'fm', 'fx', 'fy', 'fym', 'idx', 'idy', 'industry', 'mdim', 'model', 'mx_alg', 'mx_lam', 'mx_theo', 'mx_theos', 'my_alg', 'my_lam', 'my_theo', 'my_theos', 'ndim', 'nodes_full_name', 'pdim', 'qdim', 'qxdim', 'qydim', 'rat_var', 'rel_var', 'selmat', 'selvec', 'selwei', 'show_nr_indiv', 'table_company', 'tau', 'x_basevars', 'xcdat', 'xdat', 'xdat_add', 'xmean', 'xmedian', 'xvars', 'xvars_add', 'y_basevars', 'ydet', 'year', 'yhat', 'ymcdat', 'ymdat', 'ymean', 'ymedian', 'ymvars', 'ymvars_db', 'yvars']

			pa:
			['Beteiligungsquote', 'IRate', 'ISpread', 'MSLrel', 'TaxRate', 'cluster', 'country', 'deltaBasis', 'industry', 'sigma']

---
<p align="right">[Back to Top]()</p>

#### de_life_model
`Arguments: (pa_year)`

German life insurance model.

	base_var = BS  # for indiv dx, dy

	rat_var
		"MRZ": "average tariff rate",
		"BABRate": "Stock reduction rate",
		"Drift": "Drift",
		"delta": "delta",
		"x": "relative start buffer",
		"SMQuote": "Safety Fund Quota",
		"ökEKQuote": "economic equity ratio",
		"NVZ": "Net return",
		"GVZ": "sustainable total return"

	rel_var
		"PDUR": "Passive duration",
		"p": "p",
		"q": "q"

	xvars
		# exogeneous variables (20 Input variables)
		"ABWR": "active valuation reserves",
		"BS": "HGB balance sheet total",
		"BWKA": "Book value of capital investments",
		"DG": "Direct credit", # N/A
		"EKoGRNV": "HGB equity without GR and NV",
		"FLV": "Fund-linked course",
		"FreieRfB": "free RSt for premium refund",
		"GR": "Profit participation rights",
		"GewAb": "Profit transfer",
		"HGBDR": "HGB actuarial reserve",
		"JÜV": "Annual surplus before taxes and profit transfer",
		"KAA": "Investment expenses",
		"KAE": "Investment Income",
		"MRZ": "average tariff rate",
		"NV": "Subordinated Liabilities",
		"RÜE": "Risk and other result",
		"Steuer" (Tax in german): "", # Full name required
		"SÜAF": "Final profit participation fund",
		"Tax": "Taxes", # N/A
		"ZRfB": "Transfer to RfB", # N/A
		"ZVF": "Payments for insurance claims",
		"ZZR": "Additional interest reserve",
		"ZZRA": "ZZR effort"

	yvars
		# endogeneous variables (31 Output variables) 
		"Assets": "Market value balance sheet total",
		"BABRate": "Stock reduction rate",
		"Buffer": "buffer", # N/A
		"Call": "Call", # N/A
		"DR": "HGB-DRSt without ZZR",
		"DRS": "HGB-DRSt without ZZR plus FLV",
		"DT": "deferred taxes",
		"EK": "HGB equity",
		"GVZ": "sustainable total return",
		"Guarantee" (Garantie): "Guarantee",
		"GuO": "Guarantees and Options",
		"IV": "intrinsic value", # N/A
		"IVvormax": "intrinsic value before maximization", # N/A
		"JÜ": "Annual surplus after taxes and profit transfer",
		"KA": "Market value of capital investments",
		"KE": "Capital result",
		"MSL": "maximum silent loads", # N/A
		"MWDR": "Market value actuarial reserve", # N/A
		"NVZ": "Net return",
		"PBWR": "Passive valuation reserves ",
		"PDUR": "Passive duration",
		"Puffer" (Buffer in German): "", # Full name required
		"Put": "Put", # N/A
		"Putvormax": "Put before maximizing", # N/A
		"RÜ": "Gross surplus",
		"SA": "other assets",
		"SM": "Safety means",
		"SMQuote": "Safety Fund Quota",
		"SP": "other liabilities",
		"TV": "Time value", # N/A
		"VerfRfB": "available RfB",    
		"ZA": "Interest expense",
		"ZE": "Interest result",
		"ZÜ": "future surpluses",
		"ZÜKA": "future pass. Interest surplus",
		"ZÜVN": "future profit sharing ",
		"ZÜVT": "future pass. Vt. Surpluses",
		"ZÜVU": "future shareholder profits ",
		"ökEK": "economic equity",
		"ökEKQuote": "economic equity ratio"

---
<p align="right">[Back to Top]()</p>

#### de_disability_model
`Arguments: (pa_year)`

German disability insurance model

	base_var = BS  # for indiv dx, dy

	rat_var
		"MRZ": "average tariff rate",
		"BABRate": "Stock reduction rate",
		"Drift": "Drift",
		"delta": "delta",
		"x": "relative start buffer",
		"SMQuote": "Safety Fund Quota",
		"ökEKQuote": "economic equity ratio",
		"NVZ": "Net return",
		"GVZ": "sustainable total return",
		"KAZins": "", # Full name required
		"VTZins": "", # Full name required
		"VTZinsnet": "" # Full name required

	rel_var
		"PDUR": "Passive duration",
		"p": "p",
		"q": "q"

	xvars
		# exogeneous variables (20 Input variables)
		"ABWR": "active valuation reserves",
		"BS": "HGB balance sheet total",
		"BWKA": "Book value of capital investments",
		"DG": "Direct credit", # N/A
		"EKoGRNV": "HGB equity without GR and NV",
		"FLV": "Fund-linked course",
		"FreieRfB": "free RSt for premium refund",
		"GR": "Profit participation rights",
		"GewAb": "Profit transfer",
		"HGBDR": "HGB actuarial reserve",
		"JÜV": "Annual surplus before taxes and profit transfer",
		"KAA": "Investment expenses",
		"KAE": "Investment Income",
		"MRZ": "average tariff rate",
		"NV": "Subordinated Liabilities",
		"RÜE": "Risk and other result",
		"Steuer" (Tax in german): "", # Full name required
		"SÜAF": "Final profit participation fund",
		"Tax": "Taxes", # N/A
		"ZRfB": "Transfer to RfB", # N/A
		"ZVF": "Payments for insurance claims",
		"ZZR": "Additional interest reserve",
		"ZZRA": "ZZR effort"


	yvars
		# endogeneous variables (34 Output variables) 
		"Assets": "Market value balance sheet total",
		"BABRate": "Stock reduction rate",
		"Buffer": "buffer", # N/A
		"Call": "Call", # N/A
		"DR": "HGB-DRSt without ZZR",
		"DRS": "HGB-DRSt without ZZR plus FLV",
		"DT": "deferred taxes",
		"EK": "HGB equity",
		"GVZ": "sustainable total return",
		"Guarantee" (Garantie): "Guarantee",
		"GuO": "Guarantees and Options",
		"IV": "intrinsic value", # N/A
		"IVvormax": "intrinsic value before maximization", # N/A
		"JÜ": "Annual surplus after taxes and profit transfer",
		"KA": "Market value of capital investments",
		"KAZins": "", # Full name required
		"KE": "Capital result",
		"MSL": "maximum silent loads", # N/A
		"MWDR": "Market value actuarial reserve", # N/A
		"NVZ": "Net return",
		"PBWR": "Passive valuation reserves ",
		"PDUR": "Passive duration",
		"Puffer" (Buffer in German): "", # Full name required
		"Put": "Put", # N/A
		"Putvormax": "Put before maximizing", # N/A
		"RÜ": "Gross surplus",
		"SA": "other assets",
		"SM": "Safety means",
		"SMQuote": "Safety Fund Quota",
		"SP": "other liabilities",
		"TV": "Time value", # N/A
		"VTZins": "", # Full name required
		"VTZinsnet": "", # Full name required
		"VerfRfB": "available RfB",    
		"ZA": "Interest expense",
		"ZE": "Interest result",
		"ZÜ": "future surpluses",
		"ZÜKA": "future pass. Interest surplus",
		"ZÜVN": "future profit sharing ",
		"ZÜVT": "future pass. Vt. Surpluses",
		"ZÜVU": "future shareholder profits ",
		"ökEK": "economic equity",
		"ökEKQuote": "economic equity ratio"

---
<p align="right">[Back to Top]()</p>

#### graph

Understand the meaning of graphs.json content and where it is used.

Keys used in graphs.json file

		base_var: true or false
		cluster_label: Lebensversicherer (Life Insurer)
		company_ids: ["DL1001"]
		dir_path: "output/"
		direct_theo: 
		edx: 
		edy: 
		ex_indivs: 
		ex_theo: 
		exj_indivs: 
		exj_theo: 
		ey_indivs: 
		ey_theo:
		eyj_indivs:
		eyj_theo:
		eyx_indivs:
		eyx_theo:
		eyy_indivs:
		eyy_theo:
		fdx:
		fdy:
		idx:
		idy:
		is_all_graph: true or false
		model_dat_condition: true or false
		mx_indivs:
		mx_theo:
		my_indivs:
		my_theo:
		nodes_full_name:
		show_nr_indiv:
		table_company:
		xnodes:
		ynodes:
