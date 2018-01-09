import conjugate

'''
to add:
	- mi verb endings
	- optative
'''

#1st pp
pres_act_ind = ['ω', 'εις', 'ει', 'ομεν', 'ετε', 'ουσι(ν)']
pres_act_ind_epsilon_contract = ['ῶ', 'εῖς', 'εῖ', 'οῦμεν', 'εῖτε', 'οῦσι(ν)']
pres_act_ind_alpha_contract = ['ῶ', 'ᾷς', 'ᾷ', 'ῶμεν', 'ᾶτε', 'ῶσι(ν)']
pres_act_ind_omicron_contract = ['ῶ', 'οῖς', 'οῖ', 'οῦμεν', 'οῦτε', 'οῦσι(ν)']

pres_mp_ind = ['ομαι', 'ῃ', 'εται', 'όμεθα', 'εσθε', 'ονται']
pres_mp_ind_epsilon_contract = ['οῦμαι', 'ῇ', 'εῖται', 'ούμεθα', 'εῖσθε', 'οῦνται']
pres_mp_ind_alpha_contract = ['ῶμαι', 'ᾷ', 'ᾶται', 'ώμεθα', 'ᾶσθε', 'ῶνται']
pres_mp_ind_omicron_contract = ['οῦμαι', 'οῖ', 'οῦται', 'ούμεθα', 'οῦσθε', 'οῦνται']

impf_act_ind = ['ον', 'ες', 'ε(ν)', 'ομεν', 'ετε', 'ον']
impf_act_ind_epsilon_contract = ['οῦν', 'εις', 'ει', 'οῦμεν', 'εῖτε', 'ουν']
impf_act_ind_alpha_contract = ['ων', 'ας', 'α', 'ῶμεν', 'ᾶτε', 'ων']
impf_act_ind_omicron_contract = ['ουν', 'ους', 'ου', 'οῦμεν', 'οῦτε', 'ουν']

impf_mp_ind = ['όμην','ου','ετο','όμεθα','εσθε','οντο']
impf_mp_ind_epsilon_contract = ['ούμην','οῦ','εῖτο','ούμεθα','εῖσθε','οῦντο']
impf_mp_ind_alpha_contract = ['ώμην','ῶ','ᾶτο','ώμεθα','ᾶσθε','ῶντο']
impf_mp_ind_omicron_contract = ['ούμην','οῦ','οῦτο','ούμεθα','οῦσθε','οῦντο']

#2nd pp
fut_act_ind = ['ω', 'εις', 'ει', 'ομεν', 'ετε', 'ουσι(ν)']
fut_act_ind_contract = ['ῶ', 'εῖς', 'εῖ', 'οῦμεν', 'εῖτε', 'οῦσι(ν)']
fut_mid_ind = ['ομαι', 'ῃ', 'εται', 'όμεθα', 'εσθε', 'ονται']
fut_mid_ind_contract = ['οῦμαι', 'ῇ', 'εῖται', 'ούμεθα', 'εῖσθε', 'οῦνται']

#3rd pp
aor2_act_ind = ['ον', 'ες', 'ε(ν)', 'ομεν', 'ετε', 'ον']
aor2_mid_ind = ['όμην','ου','ετο','όμεθα','εσθε','οντο']
aor2_ath = ['ν', 'ς', '', 'μεν', 'τε', 'σαν']

aor1_act_ind = ['α', 'ας', 'ε(ν)', 'αμεν', 'ατε', 'αν']
aor1_mid_ind = ['άμην','ω','ατο','άμεθα','ασθε','αντο']

#4th pp
pf_act_ind = ['α', 'ας', 'ε(ν)', 'αμεν', 'ατε', 'ασι(ν)']

plupf_act_ind = ['η', 'ης', 'ει(ν)', 'εμεν', 'ετε', 'εσαν']

#5th pp
pf_mp_ind = ['μαι', 'σαι', 'ται', 'μεθα', 'σθε', 'νται']
pf_mp_ind_labial = ['μμαι', 'ψαι', 'πται', 'μμεθα', 'φθε', '(part + εἰσι(ν))']
pf_mp_ind_palatal = ['γμαι', 'ξαι', 'κται', 'γμεθα', 'χθε', '(part + εἰσι(ν))']
pf_mp_ind_dental = ['σμαι', 'σαι', 'σται', 'σμεθα', 'σθε', '(part + εἰσι(ν))']

plupf_mp_ind = ['μην', 'σο', 'το', 'μεθα', 'σθε', 'ντο']
plupf_mp_ind_labial = ['μμην', 'ψο', 'πτο', 'μμεθα', 'φθε', '(part + ἦσαν)']
plupf_mp_ind_palatal = ['γμην', 'ξο', 'κτο', 'γμεθα', 'χθε', '(part + ἦσαν)']
plupf_mp_ind_dental = ['σμην', 'σο', 'στο', 'σμεθα', 'σθε', '(part + ἦσαν)']

#6th pp
aor_pass_ind = ['ην', 'ης', 'η', 'ημεν', 'ητε', 'ησαν']
fut_pass_ind = ['ήσομαι', 'ήσῃ/ήσει', 'ήσεται', 'ησόμεθα', 'ήσεσθε', 'ήσονται']

#subj
act_subj = ['ω', 'ῃς', 'ῃ', 'ωμεν', 'ητε', 'ωσι(ν)']
act_subj_contract = ['ῶ', 'ῇς', 'ῇ', 'ῶμεν', 'ῆτε', 'ῶσι(ν)']
mp_subj = ['ωμαι', 'ῃ', 'ηται', 'ώμεθα', 'ησθε', 'ωνται']

#opt
pres_act_opt = ['οιμι', 'οις', 'οι', 'οιμεν', 'οιτε', 'οιεν']
pres_act_opt_epsilon_contract = ['οίην', 'οίης', 'οίη', 'οῖμεν', 'οῖτε', 'οῖεν']
pres_act_opt_epsilon_alt = ['οῖμι', 'οῖς', 'οῖ', 'οίημεν', 'οίητε', 'οίησαν']
pres_act_opt_alpha_contract = ['ῴην', 'ῴης', 'ῷη', 'ῷμεν', 'ῷτε', 'ῷεν']
pres_act_opt_alpha_alt = ['ῷμι', 'ῷς', 'ῷ', 'ῴημεν', 'ῴητε', 'ῷησαν']
pres_act_opt_omicron_contract = ['οίην', 'οίης', 'οίη', 'οῖμεν', 'οῖτε', 'οῖεν']
pres_act_opt_omicron_alt = ['οῖμι', 'οῖς', 'οῖ', 'οίημεν', 'οίητε', 'οίησαν']

pres_mp_opt = ['οίμην', 'οιο', 'οιτο', 'οίμεθα', 'οισθε', 'οιντο']
pres_mp_opt_epsilon_contract = ['οίμην', 'οῖο', 'οῖτο', 'οίμεθα', 'οῖσθε', 'οῖντο']
pres_mp_opt_alpha_contract = ['ῴμην', 'ῷο', 'ῷτο', 'ῴμεθα', 'ῷσθε', 'ῷντο']
pres_mp_opt_omicron_contract = ['οίμην', 'οῖο', 'οῖτο', 'οίμεθα', 'οῖσθε', 'οῖντο']

fut_act_opt = ['οιμι', 'οις', 'οι', 'οιμεν', 'οιτε', 'οιεν']
fut_mid_opt = ['οίμην', 'οιο', 'οιτο', 'οίμεθα', 'οισθε', 'οιντο']
fut_pass_opt = ['ησοίμην', 'ήσοιο', 'ήσοιτο', 'ησοίμεθα', 'ήσοισθε', 'ήσοιντο']

aor1_act_opt = ['αιμι', 'αις/ειας', 'αι/ειε', 'αιμεν', 'αιτε', 'αιεν/ειαν']
aor1_mid_opt = ['αίμην', 'αιο', 'αιτο', 'αίμεθα', 'αισθε', 'αιντο']

aor2_act_opt = ['οιμι', 'οις', 'οι', 'οιμεν', 'οιτε', 'οιεν']
aor2_mid_opt = ['οίμην', 'οιο', 'οιτο', 'οίμεθα', 'οισθε', 'οιντο']

pf_act_opt = ['οιμι', 'οις', 'οι', 'οιμεν', 'οιτε', 'οιεν']

aor_pass_opt = ['είην', 'είης', 'είη', 'εῖμεν', 'εῖτε', 'εῖεν']

#imp
pres_act_imp = ['ε', 'έτω', 'ετε', 'όντων']
pres_act_imp_epsilon = ['ει', 'είτω', 'εῖτε', 'ούντων']
pres_act_imp_alpha = ['α', 'άτω', 'ᾶτε', 'ώντων']
pres_act_imp_omicron = ['ου', 'ούτω', 'οῦτε', 'ούντων']

pres_mp_imp = ['ου', 'έσθω', 'εσθε', 'έσθων']
pres_mp_imp_epsilon = ['οῦ', 'είσθω', 'εῖσθε', 'είσθων']
pres_mp_imp_alpha = ['ῶ', 'άσθω', 'ᾶσθε', 'άσθων']
pres_mp_imp_omicron = ['οῦ', 'ούσθω', 'οῦσθε', 'ούσθων']

aor1_act_imp = ['ον', 'άτω', 'ατε', 'άντων']
aor1_mid_imp = ['αι', 'άσθω', 'ασθε', 'άσθων']

aor2_act_imp = ['ε', 'έτω', 'ετε', 'όντων']
aor2_mid_imp = ['οῦ', 'έσθω', 'εσθε', 'έσθων']

#inf
pres_act_inf = ['ειν']
pres_act_inf_epsilon = ['εῖν']
#pres_act_inf_alpha = 
#pres_act_inf_omicron =

pres_mp_inf = ['εσθαι']
pres_mp_inf_epsilon = ['εῖσθαι']
#pres_mp_inf_alpha = 
#pres_mp_inf_omicron = 

fut_act_inf = ['ειν']
fut_act_inf_contract = ['εῖν']
fut_mid_inf = ['εσθαι']

aor1_act_inf = ['αι']
aor2_act_inf = ['εῖν']

#aor1_mid_inf = 
aor2_mid_inf = ['έσθαι']

pf_act_inf = ['έναι']

pf_mp_inf = ['σθαι']
#pf_mp_inf_dental = 
pf_mp_inf_palatal = ['χθαι']
#pf_mp_ind_labial = 

aor_pass_inf = ['ῆναι']
fut_pass_inf = ['ήσεσθαι']

#mi-verbs


'''
stem and ending list pairs

completely_regular_verb = [

	(pp1, pres_act_ind),
	(pp1, act_subj), #pres
	(pp1, pres_act_opt),
	(pp1, pres_act_inf),
	(pp1, pres_act_imp),
	(pp1, pres_mp_ind),
	(pp1, mp_subj), #pres
	(pp1, pres_mp_opt),
	(pp1, pres_mp_inf),
	(pp1, pres_mp_imp),
	(pp1_aug, impf_act_ind),
	(pp1_aug, impf_mp_ind),

	(pp2, fut_act_ind),
	(pp2, fut_act_opt),
	(pp2, fut_act_inf),
	(pp2, fut_mid_ind),
	(pp2, fut_mid_opt),
	(pp2, fut_mid_inf),

	(pp3, aor1_act_ind),
	(pp3, act_subj), #aor
	(pp3, aor1_act_opt),
	(pp3, aor1_act_inf),
	(pp3, aor1_act_imp),
	(pp3, aor1_mid_ind),
	(pp3, mp_subj), #aor
	(pp3, aor1_mid_opt),
	(pp3, aor1_mid_inf),
	(pp3, aor1_mid_imp),

	(pp4, pf_act_ind),
	(pp4, act_subj), #pf
	(pp4, pf_act_opt),
	(pp4, pf_act_inf),
	(pp4_aug, plupf_act_ind),

	(pp5, pf_mp_ind),
	(pp5, pf_mp_inf),
	(pp5_aug, plupf_mp_ind),

	(pp6, aor_pass_ind),
	(pp6, act_subj_contract), #aor pass
	(pp6, aor_pass_opt),
	(pp6, aor_pass_inf),
	(pp6, fut_pass_ind),
	(pp6, fut_pass_opt),
	(pp6, fut_pass_inf)
]
'''

ἄγω = [ #DONE
	('ἀγ', pres_act_ind),
	('ἀγ', pres_mp_ind),
	('ἠγ', impf_act_ind),
	('ἠγ', impf_mp_ind),
	('ἀξ', fut_act_ind),
	('ἀξ', fut_mid_ind),
	('ἠγαγ', aor2_act_ind),
	('ἠγαγ', aor2_mid_ind),
	('ἠχ', pf_act_ind),
	('ἠχ', plupf_act_ind),
	('ἠ', pf_mp_ind_palatal),
	('ἠ', plupf_mp_ind_palatal),
	('ἠχθ', aor_pass_ind),
	('ἀχθ', fut_pass_ind),
	('ἀγ', act_subj),
	('ἀγ', mp_subj),
	('ἀγ', pres_act_opt),
	('ἀγ', pres_mp_opt),
	('ἀγ', pres_act_inf),
	('ἀγ', pres_mp_inf),
	('ἀξ', fut_act_opt),
	('ἀξ', fut_mid_opt),
	('ἀξ', fut_act_inf),
	('ἀξ', fut_mid_inf),
	('ἀγάγ', act_subj),
	('ἀγάγ', mp_subj),
	('ἀγάγ', aor2_act_opt),
	('ἀγάγ', aor2_mid_opt),
	('ἀγάγ', aor2_act_inf),
	('ἀγάγ', aor2_mid_inf),
	('ἠχ', act_subj),
	('ἠχ', pf_act_opt),
	('ἠχ', pf_act_inf),
	('ἠ', pf_mp_inf_palatal),
	('ἀχθ', act_subj),
	('ἀχθ', aor_pass_opt),
	('ἀχθ', aor_pass_inf),
	('ἀχθ', fut_pass_opt),
]

βαίνω = [ #DONE
	('βαιν', pres_act_ind),
	('ἐβαιν', impf_act_ind),
	('βησ', fut_mid_ind),
	('ἐβη', aor2_ath),
	('βεβηκ', pf_act_ind),
	('ἐβεβηκ', plupf_act_ind),
	('βαιν', act_subj),
	('βαιν', mp_subj),
	('βαιν', pres_act_opt),
	('βαιν', pres_mp_opt),
	('βαιν', pres_act_inf),
	('βαιν', pres_mp_inf),
	('βησ', fut_mid_opt),
	('β', act_subj_contract),
	('βαι', ['ην', 'ης', 'η', 'μεν', 'τε', 'εν']), #aor opt
	('βῆν', aor1_act_inf),
	('βεβήκ', act_subj), #pf
	('βεβήκ', pf_act_opt),
	('βέβηκ', pf_act_inf),
	('β', fut_pass_opt),
	('βησ', fut_mid_inf)
]

βάλλω = [ #DONE
	('βαλλ', pres_act_ind),
	('βαλλ', pres_mp_ind),
	('ἐβαλλ', impf_act_ind),
	('ἐβαλλ', impf_mp_ind),
	('βαλ', fut_act_ind_contract),
	('βαλ', fut_mid_ind_contract),
	('ἐβαλ', aor2_act_ind),
	('ἐβαλ', aor2_mid_ind),
	('βεβληκ', pf_act_ind),
	('ἐβεβληκ', plupf_act_ind),
	('βεβλη', pf_mp_ind),
	('ἐβεβλη', plupf_mp_ind),
	('ἐβληθ', aor_pass_ind),
	('βληθ', fut_pass_ind),
	('βάλλ', act_subj), #pres
	('βάλλ', pres_act_opt),
	('βάλλ', pres_act_inf),
	('βάλλ', mp_subj), #pres
	('βάλλ', pres_mp_opt),
	('βάλλ', pres_mp_inf),
	('βαλ', fut_act_opt),
	('βαλ', fut_act_inf_contract),
	('βαλ', fut_mid_opt),
	('βαλ', fut_mid_inf),
	('βάλ', act_subj), #aor
	('βαλ', aor2_act_opt),
	('βαλ', aor2_act_inf),
	('βαλ', mp_subj),
	('βαλ', aor2_mid_opt),
	('βαλ', aor2_mid_inf),
	('βεβληκ', act_subj), #pf
	('βεβληκ', pf_act_opt),
	('βεβληκ', pf_act_inf),
	('βεβλη', pf_mp_inf),
	('βληθ', act_subj_contract), #aor pass
	('βληθ', aor_pass_opt),
	('βληθ', aor_pass_inf),
	('βληθ', fut_pass_opt),
	('βληθ', fut_pass_inf)
]

δίδωμι = [
	('διδ', ['ωμι', 'ως', 'ωσι', 'ομεν', 'οτε', 'οασι']),
	('διδ', ['ῶ', 'ῷς', 'ῷ', 'ῶμεν', 'ῶτε', 'ῶσι']),
	('διδ', pres_act_opt_epsilon_contract),
	('διδ', ['όναι']),
	('διδ', ['ου', 'οτε']),
	('διδο', pf_mp_ind), #pres mp ind
	('διδ', ['ῶμαι', 'ῷ', 'ῶται', 'ώμεθα', 'ῶσθε', 'ῶνται']), #pres
	('διδ', pres_mp_opt),
	('δίδ', ['οσθαι']),
	('δίδ', ['οσο', 'οσθε']),
	('ἐδίδο', ['υν', 'υς', 'υ', 'μεν', 'τε', 'σαν']),
	('ἐδιδο', plupf_mp_ind), #impf mp ind

	('δώσ', fut_act_ind),
	('δώσ', fut_act_opt),
	('δώσ', fut_act_inf),
	('δώσ', fut_mid_ind),
	('δώσ', fut_mid_opt),
	('δώσ', fut_mid_inf),

	('ἔδ', ['ωκα', 'ωκας', 'ωκα', 'ομεν', 'οτε', 'ωκαν']),
	('δ', ['ῶ', 'ῷς', 'ῷ', 'ῶμεν', 'ῶτε', 'ῶσι']), #aor
	('δ', pres_act_opt_epsilon_contract), #aor act opt
	('δ', ['οῦναι']),
	('δ', ['ός', 'ότε']),
	('δ', ['ῶμαι', 'ῷ', 'ῶται', 'ώμεθα', 'ῶσθε', 'ῶνται']), #aor act subj
	('ἐδο', ['μην', 'υ', 'το', 'μεθα', 'σθε', 'ντο']),
	('δ', pres_mp_opt_omicron_contract), #aor mid opt
	('δό', pf_mp_inf), #aor mid inf
	('δ', ['οῦ', 'όσθε']),

	('δεδωκ', pf_act_ind),
	('δεδωκ', act_subj), #pf
	('δεδωκ', pf_act_opt),
	('δεδωκ', pf_act_inf),
	('ἐδεδωκ', plupf_act_ind),

	('δεδο', pf_mp_ind),
	('δεδο', pf_mp_inf),
	('ἐδεδο', plupf_mp_ind),

	('ἐδόθ', aor_pass_ind),
	('δοθ', act_subj_contract), #aor pass
	('δοθ', aor_pass_opt),
	('δοθ', aor_pass_inf),
	('δοθ', fut_pass_ind),
	('δοθ', fut_pass_opt),
	('δοθ', fut_pass_inf)
]

ἔρχομαι = [
	('ἐρχ', pres_mp_ind),
	('ἐρχ', mp_subj),
	('ἐρχ', pres_mp_opt),
	('ἐρχ', pres_mp_inf),
	('ἔρχ', ['οσο', 'οσθε']),
	('ἠρχ', impf_mp_ind),

	('ἐλευσ', fut_mid_ind),
	('ἐλε', ['οίμην', 'ύσοιο', 'ύσοιτο', 'οίμεθα', 'ύσοισθε', 'ύσοιντο']), #fut opt
	('ἐλεύσ', fut_mid_inf),

	('ἠλθ', aor2_act_ind),
	('ἔλθ', act_subj), #aor subj
	('ἔλθ', aor2_act_opt),
	('ἐλθ', aor2_act_inf),
	('ἐλθ', ['έ', 'ετε']),

	('ἐληλυθ', pf_act_ind),
	('ἐληλύθ', act_subj),
	('ἐληλύθ', pf_act_opt),
	('ἐληλύθ', pf_act_inf),
	('ἠληλύθ', plupf_act_ind)
]

ἔχω = [

]

ἵστημι = [

] 

ὁράω = [

]

τίθημι = [

]

φημί = [

]

print(conjugate.full_conjugate(ἔρχομαι))
