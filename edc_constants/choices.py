from django.utils.translation import gettext as _

from .constants import (
    ALIVE, DEAD, DECLINED, DWTA, FEMALE, IND, MALE, NAIVE,
    NEG, NEVER, NO, NOT_APPLICABLE, OMANG, OTHER, POS, REFUSED, UNKNOWN, YES,
    MORNING, AFTERNOON, EVENING, ANYTIME, WEEKDAYS, WEEKENDS,
    NOT_SURE, NORMAL, ABNORMAL, NOT_DONE)


BLANK_CHOICE_DASH = [('', '---------')]

""" Try to keep these in alphabetical order
"""

ACU_EST = (
    ('Acute', 'Acute'),
    ('Established', 'Established'),
)

ACU_EST_NEG = (
    ('Acute', 'Acute'),
    ('Established', 'Established'),
    ('Negative', 'Negative'),
)

ALIVE_DEAD = (
    (ALIVE, 'Alive'),
    (DEAD, 'Dead'),
)

ALIVE_DEAD_UNKNOWN = (
    (ALIVE, 'Alive'),
    (DEAD, 'Deceased'),
    (UNKNOWN, 'Unknown'),
)

ART_STATUS = (
    ('ON', 'Yes, on ART'),
    ('STOPPED', 'No, stopped ART'),
    (NAIVE, 'No, have never taken ART'),
)

ART_STATUS_UNKNOWN = (
    ('ON', 'ON ART'),
    ('STOPPED', 'Stopped'),
    (NAIVE, 'Naive'),
    (UNKNOWN, 'Unknown'),

)

ART_STATUS_CONFIRM = (
    ('OPD', '1. Show OPD/IDCC card'),
    ('Pills', '2. Show pills'),
    ('Pic', '3. Identify pictorial'),
)

CONFIRMED_SUSPECTED = (
    ('CONFIRMED', 'Confirmed'),
    ('SUSPECTED', 'Suspected'),
)

COUNTRY = (
    ('botswana', 'Botswana'),
    ('zimbabwe', 'Zimbabwe'),
    ('rsa', 'South Africa'),
    ('zambia', 'Zambia'),
    ('namibia', 'Namibia'),
    ('nigeria', 'Nigeria'),
    ('china', 'China'),
    ('india', 'India'),
    ('OTHER', 'Other'),
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    ('AnyDay', 'Any day'),
)


DATE_ESTIMATED = (
    ('-', 'No'),
    ('D', 'Yes, estimated the Day'),
    ('MD', 'Yes, estimated Month and Day'),
    ('YMD', 'Yes, estimated Year, Month and Day'),
)

DEATH_RELATIONSIP_TO_STUDY = (
    ('Definitely not related', 'Definitely not related'),
    ('Probably not related', 'Probably not related'),
    ('Possible related', 'Possible related'),
    ('Probably related', 'Probably related'),
    ('Definitely related', 'Definitely related')
)


FEEDING = (
    ('BF', 'Breast feed'),
    ('FF', 'Formula feed'),
)

GENDER = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
)

GENDER_UNDETERMINED = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
    ('U', _('Undetermined')),
)

GRADING_SCALE = (
    (1, 'Grade 1'),
    (2, 'Grade 2'),
    (3, 'Grade 3'),
    (4, 'Grade 4'),
    (5, 'Grade 5'),
)

GRADING_SCALE_234 = (
    (2, 'Grade 2'),
    (3, 'Grade 3'),
    (4, 'Grade 4'),
)

GRADING_SCALE_34 = (
    (3, 'Grade 3'),
    (4, 'Grade 4'),
)

HIV_RESULT = (
    (POS, 'HIV Positive (Reactive)'),
    (NEG, 'HIV Negative (Non-reactive)'),
    (IND, 'Indeterminate'),
    (DECLINED, 'Participant declined testing'),
    ('Not performed',
     'Test could not be performed (e.g. supply outage, technical problem)'),
)

"""do not change without inspecting implication to check_omang_field() in utils.py"""
IDENTITY_TYPE = (
    (OMANG, 'Omang'),
    ('DRIVERS', 'Driver\'s License'),
    ('PASSPORT', 'Passport'),
    ('OMANG_RCPT', 'Omang Receipt'),
    (OTHER, 'Other'),
)


NORMAL_ABNORMAL = (
    (NORMAL, 'Normal'),
    (ABNORMAL, 'Abnormal'),
)

NORMAL_ABNORMAL_NOEXAM = (
    (NORMAL, 'Normal'),
    (ABNORMAL, 'Abnormal'),
    ('NO_EXAM', 'No exam performed'),
)

NORMAL_ABNORMAL_NOTEVALUATED = (
    (NORMAL, 'Normal'),
    (ABNORMAL, 'Abnormal'),
    ('NOT_EVAL', 'Not evaluated'),
)

POS_NEG = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    (IND, 'Indeterminate'),
)

POS_NEG_REFUSED = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    (IND, 'Indeterminate'),
    ('REF', 'Refused to disclose'),
)

POS_NEG_ANY = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    ('ANY', 'Any'),
)

POS_NEG_ONLY = (
    (POS, _('Positive')),
    (NEG, _('Negative')),
)

POS_NEG_UNKNOWN = (
    (POS, _('Positive')),
    (NEG, _('Negative')),
    (UNKNOWN, _('Unknown')),
)

POS_NEG_IND_UNKNOWN = (
    (POS, _('Positive')),
    (NEG, _('Negative')),
    (IND, 'Indeterminate'),
    (UNKNOWN, _('Unknown')),
)

POS_NEG_ACU = (
    ('Positive', 'Positive'),
    ('Negative', 'Negative'),
    ('Possible Acute', 'Possible acute'),
    ('Indeterminate', 'Indeterminate'),
)

POS_NEG_NOTESTED = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    (NEVER, 'Never tested for HIV'),
)


POS_NEG_UNTESTED_REFUSAL = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    (IND, 'Indeterminate'),
    (NEVER, 'Never tested for HIV'),
    (UNKNOWN, 'Unknown'),
    (DWTA, 'Don\'t want to answer'),
)

REFUSAL_STATUS = (
    (REFUSED, 'Refused'),
    ('NOT_REFUSED', 'No longer refusing'),
)

SEVERITY_LEVEL = (
    ('mild', 'Mild'),
    ('moderate', 'Moderate'),
    ('severe', 'Severe'),
)

SEXUAL_DEBUT = (
    ('<=14', '14 or under'),
    ('15-17', ' 15 - 17'),
    ('>=18', '18 or above'),
)

TIME_OF_WEEK = (
    (WEEKDAYS, 'Weekdays'),
    (WEEKENDS, 'Weekends'),
    (ANYTIME, 'Anytime')
)

TIME_OF_DAY = (
    (MORNING, 'Morning'),
    (AFTERNOON, 'Afternoon'),
    (EVENING, 'Evening'),
    (ANYTIME, 'Anytime')
)

TIME_UNITS = (
    ('TODAY', 'Today'),
    ('DAYS', 'Days'),
    ('WEEKS', 'Weeks'),
    ('MONTHS', 'Months'),
    ('YEARS', 'Years'),
)

URINALYSIS = (
    ('NAD', 'NAD'),
    ('Sugar Neg', 'Sugar Neg'),
    ('Sugar +', 'Sugar +'),
    ('Sugar ++', 'Sugar ++'),
    ('Sugar +++', 'Sugar +++'),
    ('Blood', 'Blood'),
    ('Protein', 'Protein'),
    ('Cells', 'Cells'),
)

YES_NO = (
    (YES, _(YES)),
    (NO, _(NO)),
)

YES_NO_DECLINED = (
    (YES, YES),
    (NO, NO),
    (DECLINED, 'Yes, but subject declined copy'),
)

YES_NO_OPTIONAL = (
    (YES, YES),
    (NO, NO),
    ('Optional', 'Optional'),
)

YES_NO_REFUSED = (
    (YES, _(YES)),
    (NO, _(NO)),
    (REFUSED, _('Refused to answer')),
)

YES_NO_DWTA = (
    (YES, _(YES)),
    (NO, _(NO)),
    (DWTA, _('Don\'t want to answer')),
)

YES_NO_NA_SPECIFY = (
    (YES, 'Yes, (Specify below)'),
    (NO, NO),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_NA = (
    (YES, YES),
    (NO, NO),
    (NOT_APPLICABLE, 'Not applicable'),
)


YES_NO_NA_DWTA = (
    (YES, _(YES)),
    (NO, _(NO)),
    (DWTA, _('Don\'t want to answer')),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_NA_DWTA_DNK = (
    (YES, _(YES)),
    (NO, _(NO)),
    (DWTA, _('Don\'t want to answer')),
    ('cant_remember', 'Cannot remember'),
)

YES_NO_NOT_EVALUATED = (
    (YES, YES),
    (NO, NO),
    ('Not_evaluated', 'Not evaluated'),
)

YES_NO_NOT_EVALUATED_NA = (
    (YES, YES),
    (NO, NO),
    ('Not_evaluated', 'Not evaluated'),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_NOT_DONE = (
    (YES, YES),
    (NO, NO),
    (NOT_DONE, 'Not done'),
)

YES_NO_DOESNT_WORK = (
    (YES, YES),
    (NO, NO),
    ('DontWork', 'Doesn\'t work'),
)

YES_NO_UNKNOWN = (
    (YES, YES),
    (NO, NO),
    (UNKNOWN, 'Unknown'),
)

YES_NO_NA_DWTA_DNK = (
    (YES, _(YES)),
    (NO, _(NO)),
    (DWTA, _('Don\'t want to answer')),
    ('cant_remember', 'Cannot remember'))

YES_NO_UNKNOWN_NA = (
    (YES, YES),
    (NO, NO),
    (UNKNOWN, 'Unknown'),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_UNSURE = (
    (YES, YES),
    (NO, NO),
    (NOT_SURE, 'Not sure'),
)

YES_NO_UNSURE_DWTA = (
    (YES, YES),
    (NO, NO),
    (NOT_SURE, 'Not sure'),
    (DWTA, 'Don\'t want to answer')
)

YES_NO_UNSURE_NA = (
    (YES, YES),
    (NO, NO),
    (NOT_SURE, 'Not sure'),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_DONT_KNOW = (
    (YES, YES),
    (NO, NO),
    ('Dont_know', 'Do not know'),
)

YES_NO_DONT_KNOW_NA = (
    (YES, YES),
    (NO, NO),
    ('Dont_know', 'Do not know'),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_DOESNT_WORK = (
    (YES, YES),
    (NO, NO),
    ('Doesnt_work', 'Doesn\'t work'),
)

ARV_DRUG_LIST = (
    ('Nevirapine', 'NVP'),
    ('Kaletra', 'KAL'),
    ('Aluvia', 'ALU'),
    ('Truvada', 'TRV'),
    ('Tenoforvir', 'TDF',),
    ('Zidovudine', 'AZT'),
    ('Lamivudine', '3TC'),
    ('Efavirenz', 'EFV'),
    ('Didanosine', 'DDI'),
    ('Stavudine', 'D4T'),
    ('Nelfinavir', 'NFV'),
    ('Abacavir', 'ABC'),
    ('Combivir', 'CBV'),
    ('Ritonavir', 'RTV'),
    ('Trizivir', 'TZV'),
    ('Raltegravir', 'RAL'),
    ('Saquinavir,soft gel capsule', 'FOR'),
    ('Saquinavir,hard capsule', 'INV'),
    ('Kaletra or Aluvia', 'KAL or ALU'),
    ('Atripla', 'ATR'),
    ('HAART,unknown', 'HAART,unknown'),
)

ARV_MODIFICATION_REASON = (
    ('Initial dose', 'Initial dose'),
    ('Never started', 'Never started'),
    ('Toxicity decreased_resolved', 'Toxicity decreased/resolved'),
    ('Completed PMTCT intervention', 'Completed PMTCT intervention'),
    ('Completed postpartum tail', 'Completed post-partum "tail"'),
    ('Scheduled dose increase', 'Scheduled dose increase'),
    ('Confirmed infant HIV infection, ending study drug',
     'Confirmed infant HIV infection, ending study drug'),
    ('completed protocol',
     'Completion of protocol-required period of study treatment'),
    ('HAART not available', 'HAART not available'),
    ('Anemia', 'Anemia'),
    ('Bleeding', 'Bleeding'),
    ('CNS symptoms', 'CNS symptoms (sleep, psych, etc)'),
    ('Diarrhea', 'Diarrhea'),
    ('Fatigue', 'Fatigue'),
    ('Headache', 'Headache'),
    ('Hepatotoxicity', 'Hepatotoxicity'),
    ('Nausea', 'Nausea'),
    ('Neutropenia', 'Neutropenia'),
    ('Thrombocytopenia', 'Thrombocytopenia'),
    ('Vomiting', 'Vomiting'),
    ('Rash', 'Rash'),
    ('Rash resolved', 'Rash resolved'),
    ('Neuropathy', 'Neuropathy'),
    ('Hypersensitivity_allergic reaction',
     'Hypersensitivity / allergic reaction'),
    ('Pancreatitis', 'Pancreatitis'),
    ('Lactic Acidiosis', 'Lactic Acidiosis'),
    ('Pancytopenia', 'Pancytopenia'),
    ('Virologic failure', 'Virologic failure'),
    ('Immunologic failure', 'Immunologic failure(CD4)'),
    ('Clinical failure', 'Clinical failure'),
    ('Clinician request',
     'Clinician request, other reason (including convenience)'),
    ('Subject request',
     'Subject request, other reason (including convenience)'),
    ('Non-adherence with clinic visits', 'Non-adherence with clinic visits'),
    ('Non-adherence with ARVs', 'Non-adherence with ARVs'),
    ('Death', 'Death'),
    (OTHER, 'Other'),
)

ARV_STATUS = (
    ('no_mod', '1. No modifications made to existing HAART treatment',),
    ('start',
     '2. Started antriretroviral treatment since last attended scheduled visit(including today)',),
    ('discontinued',
     '3. Permanently discontinued antiretroviral treatment at or before last study visit',),
    ('modified', ('4. Change in at least one antiretroviral medication since last '
                  'attended scheduled visit (including today)(dose modification, '
                  'permanent discontinuation, temporary hold, resumption / initiation '
                  'after temporary hold)'),),
)

ARV_STATUS_WITH_NEVER = (

    ('no_mod',
     '1. No modifications made since the last attended scheduled visit or today'),
    ('start',
     '2. Starting today or has started since last attended scheduled visit'),
    ('discontinued',
     '3. Permanently discontinued at or before the last attended scheduled visit'),
    ('never started', '4. Never started'),
    ('modified',
     '5. Change in at least one medication since the last attended scheduled visit or today'),
    (NOT_APPLICABLE, 'Not applicable'),
)

DOSE_STATUS = (
    ('New', 'New'),
    ('Permanently discontinued', 'Permanently discontinued'),
    ('Temporarily held', 'Temporarily held'),
    ('Dose modified', 'Dose modified'),
    ('Resumed', 'Resumed'),
    ('Not initiated', 'Not initiated'),
)

WHYNOPARTICIPATE_CHOICE = (
    ('I don\'t have time', _('I don\'t have time')),
    ('I don\'t want to answer the questions',
     _('I don\'t want to answer the questions')),
    ('I don\'t want to have the blood drawn',
     _('I don\'t want to have the blood drawn')),
    ('I am afraid my information will not be private',
     _('I am afraid my information will not be private')),
    ('Fear of needles', _('Fear of needles')),
    ('Illiterate does not want a witness',
     _('Illiterate does not want a witness')),
    ('I don\'t want to take part', _('I don\'t want to take part')),
    ('I haven\'t had a chance to think about it',
     _('I haven\'t had a chance to think about it')),
    ('Have a newly born baby, not permitted',
     _('Have a newly born baby, not permitted')),
    ('The appointment was not honoured',
     _('The appointment was not honoured')),
    ('not_sure', _('I am not sure')),
    ('OTHER', _('Other, specify:')),
    ('not_answering', _('Don\'t want to answer')),
)

COUNTRIES = (
    ('AF', 'Afghanistan',),
    ('AX', 'Aland Islands',),
    ('AL', 'Albania',),
    ('DZ', 'Algeria',),
    ('AS', 'American Samoa',),
    ('AD', 'Andorra',),
    ('AO', 'Angola',),
    ('AI', 'Anguilla',),
    ('AQ', 'Antarctica',),
    ('AG', 'Antigua and Barbuda',),
    ('AR', 'Argentina',),
    ('AM', 'Armenia',),
    ('AW', 'Aruba',),
    ('AU', 'Australia',),
    ('AT', 'Austria',),
    ('AZ', 'Azerbaijan',),
    ('BS', 'Bahamas',),
    ('BH', 'Bahrain',),
    ('BD', 'Bangladesh',),
    ('BB', 'Barbados',),
    ('BY', 'Belarus',),
    ('BE', 'Belgium',),
    ('BZ', 'Belize',),
    ('BJ', 'Benin',),
    ('BM', 'Bermuda',),
    ('BT', 'Bhutan',),
    ('BO', 'Bolivia, Plurinational State of',),
    ('BQ', 'Bonaire, Sint Eustatius and Saba',),
    ('BA', 'Bosnia and Herzegovina',),
    ('BW', 'Botswana',),
    ('BV', 'Bouvet Island',),
    ('BR', 'Brazil',),
    ('IO', 'British Indian Ocean Territory',),
    ('BN', 'Brunei Darussalam',),
    ('BG', 'Bulgaria',),
    ('BF', 'Burkina Faso',),
    ('BI', 'Burundi',),
    ('KH', 'Cambodia',),
    ('CM', 'Cameroon',),
    ('CA', 'Canada',),
    ('CV', 'Cape Verde',),
    ('KY', 'Cayman Islands',),
    ('CF', 'Central African Republic',),
    ('TD', 'Chad',),
    ('CL', 'Chile',),
    ('CN', 'China',),
    ('CX', 'Christmas Island',),
    ('CC', 'Cocos (Keeling) Islands',),
    ('CO', 'Colombia',),
    ('KM', 'Comoros',),
    ('CG', 'Congo',),
    ('CD', 'Congo, the Democratic Republic of the',),
    ('CK', 'Cook Islands',),
    ('CR', 'Costa Rica',),
    ('CI', "Cote d'Ivoire",),
    ('HR', 'Croatia',),
    ('CU', 'Cuba',),
    ('CW', 'Curacao',),
    ('CY', 'Cyprus',),
    ('CZ', 'Czech Republic',),
    ('DK', 'Denmark',),
    ('DJ', 'Djibouti',),
    ('DM', 'Dominica',),
    ('DO', 'Dominican Republic',),
    ('EC', 'Ecuador',),
    ('EG', 'Egypt',),
    ('SV', 'El Salvador',),
    ('GQ', 'Equatorial Guinea',),
    ('ER', 'Eritrea',),
    ('EE', 'Estonia',),
    ('ET', 'Ethiopia',),
    ('FK', 'Falkland Islands (Malvinas)',),
    ('FO', 'Faroe Islands',),
    ('FJ', 'Fiji',),
    ('FI', 'Finland',),
    ('FR', 'France',),
    ('GF', 'French Guiana',),
    ('PF', 'French Polynesia',),
    ('TF', 'French Southern Territories',),
    ('GA', 'Gabon',),
    ('GM', 'Gambia',),
    ('GE', 'Georgia',),
    ('DE', 'Germany',),
    ('GH', 'Ghana',),
    ('GI', 'Gibraltar',),
    ('GR', 'Greece',),
    ('GL', 'Greenland',),
    ('GD', 'Grenada',),
    ('GP', 'Guadeloupe',),
    ('GU', 'Guam',),
    ('GT', 'Guatemala',),
    ('GG', 'Guernsey',),
    ('GN', 'Guinea',),
    ('GW', 'Guinea-Bissau',),
    ('GY', 'Guyana',),
    ('HT', 'Haiti',),
    ('HM', 'Heard Island and McDonald Islands',),
    ('VA', 'Holy See (Vatican City State)',),
    ('HN', 'Honduras',),
    ('HK', 'Hong Kong',),
    ('HU', 'Hungary',),
    ('IS', 'Iceland',),
    ('IN', 'India',),
    ('ID', 'Indonesia',),
    ('IR', 'Iran, Islamic Republic of',),
    ('IQ', 'Iraq',),
    ('IE', 'Ireland',),
    ('IM', 'Isle of Man',),
    ('IL', 'Israel',),
    ('IT', 'Italy',),
    ('JM', 'Jamaica',),
    ('JP', 'Japan',),
    ('JE', 'Jersey',),
    ('JO', 'Jordan',),
    ('KZ', 'Kazakhstan',),
    ('KE', 'Kenya',),
    ('KI', 'Kiribati',),
    ('KP', "Korea, Democratic People's Republic of",),
    ('KR', 'Korea, Republic of',),
    ('KW', 'Kuwait',),
    ('KG', 'Kyrgyzstan',),
    ('LA', "Lao People's Democratic Republic",),
    ('LV', 'Latvia',),
    ('LB', 'Lebanon',),
    ('LS', 'Lesotho',),
    ('LR', 'Liberia',),
    ('LY', 'Libya',),
    ('LI', 'Liechtenstein',),
    ('LT', 'Lithuania',),
    ('LU', 'Luxembourg',),
    ('MO', 'Macao',),
    ('MK', 'Macedonia, the former Yugoslav Republic of',),
    ('MG', 'Madagascar',),
    ('MW', 'Malawi',),
    ('MY', 'Malaysia',),
    ('MV', 'Maldives',),
    ('ML', 'Mali',),
    ('MT', 'Malta',),
    ('MH', 'Marshall Islands',),
    ('MQ', 'Martinique',),
    ('MR', 'Mauritania',),
    ('MU', 'Mauritius',),
    ('YT', 'Mayotte',),
    ('MX', 'Mexico',),
    ('FM', 'Micronesia, Federated States of',),
    ('MD', 'Moldova, Republic of',),
    ('MC', 'Monaco',),
    ('MN', 'Mongolia',),
    ('ME', 'Montenegro',),
    ('MS', 'Montserrat',),
    ('MA', 'Morocco',),
    ('MZ', 'Mozambique',),
    ('MM', 'Myanmar',),
    ('NA', 'Namibia',),
    ('NR', 'Nauru',),
    ('NP', 'Nepal',),
    ('NL', 'Netherlands',),
    ('NC', 'New Caledonia',),
    ('NZ', 'New Zealand',),
    ('NI', 'Nicaragua',),
    ('NE', 'Niger',),
    ('NG', 'Nigeria',),
    ('NU', 'Niue',),
    ('NF', 'Norfolk Island',),
    ('MP', 'Northern Mariana Islands',),
    ('NO', 'Norway',),
    ('OM', 'Oman',),
    ('PK', 'Pakistan',),
    ('PW', 'Palau',),
    ('PS', 'Palestine, State of',),
    ('PA', 'Panama',),
    ('PG', 'Papua New Guinea',),
    ('PY', 'Paraguay',),
    ('PE', 'Peru',),
    ('PH', 'Philippines',),
    ('PN', 'Pitcairn',),
    ('PL', 'Poland',),
    ('PT', 'Portugal',),
    ('PR', 'Puerto Rico',),
    ('QA', 'Qatar',),
    ('RE', 'Reunion',),
    ('RO', 'Romania',),
    ('RU', 'Russian Federation',),
    ('RW', 'Rwanda',),
    ('BL', 'Saint Barthelemy',),
    ('SH', 'Saint Helena, Ascension and Tristan da Cunha',),
    ('KN', 'Saint Kitts and Nevis',),
    ('LC', 'Saint Lucia',),
    ('MF', 'Saint Martin (French part)',),
    ('PM', 'Saint Pierre and Miquelon',),
    ('VC', 'Saint Vincent and the Grenadines',),
    ('WS', 'Samoa',),
    ('SM', 'San Marino',),
    ('ST', 'Sao Tome and Principe',),
    ('SA', 'Saudi Arabia',),
    ('SN', 'Senegal',),
    ('RS', 'Serbia',),
    ('SC', 'Seychelles',),
    ('SL', 'Sierra Leone',),
    ('SG', 'Singapore',),
    ('SX', 'Sint Maarten (Dutch part)',),
    ('SK', 'Slovakia',),
    ('SI', 'Slovenia',),
    ('SB', 'Solomon Islands',),
    ('SO', 'Somalia',),
    ('ZA', 'South Africa',),
    ('GS', 'South Georgia and the South Sandwich Islands',),
    ('SS', 'South Sudan',),
    ('ES', 'Spain',),
    ('LK', 'Sri Lanka',),
    ('SD', 'Sudan',),
    ('SR', 'Suriname',),
    ('SJ', 'Svalbard and Jan Mayen',),
    ('SZ', 'Swaziland',),
    ('SE', 'Sweden',),
    ('CH', 'Switzerland',),
    ('SY', 'Syrian Arab Republic',),
    ('TW', 'Taiwan, Province of China',),
    ('TJ', 'Tajikistan',),
    ('TZ', 'Tanzania, United Republic of',),
    ('TH', 'Thailand',),
    ('TL', 'Timor-Leste',),
    ('TG', 'Togo',),
    ('TK', 'Tokelau',),
    ('TO', 'Tonga',),
    ('TT', 'Trinidad and Tobago',),
    ('TN', 'Tunisia',),
    ('TR', 'Turkey',),
    ('TM', 'Turkmenistan',),
    ('TC', 'Turks and Caicos Islands',),
    ('TV', 'Tuvalu',),
    ('UG', 'Uganda',),
    ('UA', 'Ukraine',),
    ('AE', 'United Arab Emirates',),
    ('GB', 'United Kingdom',),
    ('US', 'United States',),
    ('UM', 'United States Minor Outlying Islands',),
    ('UY', 'Uruguay',),
    ('UZ', 'Uzbekistan',),
    ('VU', 'Vanuatu',),
    ('VE', 'Venezuela, Bolivarian Republic of',),
    ('VN', 'Viet Nam',),
    ('VG', 'Virgin Islands, British',),
    ('VI', 'Virgin Islands, U.S.',),
    ('WF', 'Wallis and Futuna',),
    ('EH', 'Western Sahara',),
    ('YE', 'Yemen',),
    ('ZM', 'Zambia',),
    ('ZW', 'Zimbabwe',),
)
