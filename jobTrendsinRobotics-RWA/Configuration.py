import pandas as pd
import csv

class Configuration:
    fields = pd.DataFrame()
    careers = pd.DataFrame()
    countries = pd.DataFrame()
    continents = pd.DataFrame()
    relevant_columns = []

    def __init__(self, filename):
        self.read_config(filename)
        self.read_robotics_fields_glossary()
        self.read_robotics_careers_glossary()
        self.read_world_countries_by_identifier()
        self.read_world_countries_by_continent()
    
    #Configure relevant columns in archive excel sheet
    def read_config(self, name_dataset):
        print("Configure relevant columns in archive excel sheet")
        config = pd.read_excel(r"config.xlsx")
        config.to_csv(r"config.csv", sep=",")
        config = pd.read_csv(r"config.csv")
        self.relevant_columns = config[name_dataset+".xlsx"].tolist()
        self.relevant_columns = [x for x in self.relevant_columns if str(x) != 'nan']

    #Configure fields glossary
    def read_robotics_fields_glossary(self):
        print("Configure fields glossary")
        fields = pd.read_excel(r"robotics_fields_glossary.xlsx")
        fields.to_csv(r"robotics_fields_glossary.csv", sep=",")
        fields = pd.read_csv(r"robotics_fields_glossary.csv")
        artificial_intelligence = fields['artificial intelligence'].tolist()
        automation = fields['automation'].tolist()
        biocybernetics = fields['biocybernetics'].tolist()
        design_and_control = fields['design and control'].tolist()
        digital_electronics_and_microprocessors = fields['digital electronics and microprocessors'].tolist()
        medical_robotics = fields['medical robotics'].tolist()
        microrobotics = fields['microrobotics'].tolist()
        operator_interface = fields['operator interface'].tolist()
        programming_f = fields['programming'].tolist()
        robot_locomotion_and_mobility = fields['robot locomotion and mobility'].tolist()
        robot_manipulators_and_effectors = fields['robot manipulators and effectors'].tolist()
        sensing_and_perception = fields['sensing and perception'].tolist()
        self.fields['artificial intelligence'] = artificial_intelligence
        self.fields['automation'] = automation
        self.fields['biocybernetics'] = biocybernetics
        self.fields['design and control'] = design_and_control
        self.fields['digital electronics and microprocessors'] = digital_electronics_and_microprocessors
        self.fields['medical robotics'] = medical_robotics
        self.fields['microrobotics'] = microrobotics
        self.fields['operator interface'] = operator_interface
        self.fields['programming'] = programming_f
        self.fields['robot locomotion and mobility'] = robot_locomotion_and_mobility
        self.fields['robot manipulators and effectors'] = robot_manipulators_and_effectors
        self.fields['sensing and perception'] = sensing_and_perception

    #Configure careers glossary
    def read_robotics_careers_glossary(self):
        print("Configure careers glossary")
        careers = pd.read_excel(r"robotics_careers_glossary.xlsx")
        careers.to_csv(r"robotics_careers_glossary.csv", sep=",")
        careers = pd.read_csv(r"robotics_careers_glossary.csv")
        academia = careers['academia'].tolist()
        industry = careers['industry'].tolist()
        managerial_positions = careers['managerial positions'].tolist()
        research = careers['research'].tolist()
        self.careers['academia'] = academia
        self.careers['industry'] = industry
        self.careers['managerial positions'] = managerial_positions
        self.careers['research'] = research

    #Configure countries by identifier
    def read_world_countries_by_identifier(self):
        print("Configure countries by identifier")
        countries = pd.read_excel(r"world_countries_by_identifier.xlsx")
        countries.to_csv(r"world_countries_by_identifier.csv", sep=",")
        countries = pd.read_csv(r"world_countries_by_identifier.csv")
        afghanistan = countries['afghanistan'].tolist()
        albania	= countries['albania'].tolist()
        algeria	= countries['algeria'].tolist()
        american_samoa = countries['american samoa'].tolist()
        andorra	= countries['andorra'].tolist()
        angola	= countries['angola'].tolist()
        antarctica	= countries['antarctica'].tolist()
        antigua_and_barbuda	= countries['antigua and barbuda'].tolist()
        argentina	= countries['argentina'].tolist()
        armenia	= countries['armenia'].tolist()
        australia	= countries['australia'].tolist()
        austria	= countries['austria'].tolist()
        azerbaijan	= countries['azerbaijan'].tolist()
        bahamas	= countries['bahamas'].tolist()
        bahrain	= countries['bahrain'].tolist()
        bangladesh	= countries['bangladesh'].tolist()
        barbados	= countries['barbados'].tolist()
        belarus	= countries['belarus'].tolist()
        belgium	= countries['belgium'].tolist()
        belize	= countries['belize'].tolist()
        benin	= countries['benin'].tolist()
        bhutan	= countries['bhutan'].tolist()
        bolivia	= countries['bolivia'].tolist()
        bosnia_and_herzegovina	= countries['bosnia and herzegovina'].tolist()
        botswana	= countries['botswana'].tolist()
        brazil	= countries['brazil'].tolist()
        brunei	= countries['brunei'].tolist()
        bulgaria	= countries['bulgaria'].tolist()
        burkina_faso	= countries['burkina faso'].tolist()
        burundi	= countries['burundi'].tolist()
        cambodia	= countries['cambodia'].tolist()
        cameroon	= countries['cameroon'].tolist()
        canada	= countries['canada'].tolist()
        cape_verde	= countries['cape verde'].tolist()
        central_african_republic	= countries['central african republic'].tolist()
        chad	= countries['chad'].tolist()
        chile	= countries['chile'].tolist()
        china	= countries['china'].tolist()
        colombia	= countries['colombia'].tolist()
        comoros	= countries['comoros'].tolist()
        costa_rica	= countries['costa rica'].tolist()
        croatia	= countries['croatia'].tolist()
        cuba	= countries['cuba'].tolist()
        cyprus	= countries['cyprus'].tolist()
        czech_republic	= countries['czech republic'].tolist()
        democratic_republic_of_the_congo	= countries['democratic republic of the congo'].tolist()
        denmark	= countries['denmark'].tolist()
        djibouti	= countries['djibouti'].tolist()
        dominica	= countries['dominica'].tolist()
        dominican_republic	= countries['dominican republic'].tolist()
        ecuador	= countries['ecuador'].tolist()
        egypt	= countries['egypt'].tolist()
        el_salvador	= countries['el salvador'].tolist()
        equatorial_guinea	= countries['equatorial guinea'].tolist()
        eritrea = countries['eritrea'].tolist()
        estonia	= countries['estonia'].tolist()
        eswatini	= countries['eswatini'].tolist()
        ethiopia	= countries['ethiopia'].tolist()
        fiji	= countries['fiji'].tolist()
        finland	= countries['finland'].tolist()
        france	= countries['france'].tolist()
        gabon	= countries['gabon'].tolist()
        gambia	= countries['gambia'].tolist()
        georgia	= countries['georgia'].tolist()
        germany	= countries['germany'].tolist()
        ghana	= countries['ghana'].tolist()
        greece	= countries['greece'].tolist()
        grenada	= countries['grenada'].tolist()
        guatemala	= countries['guatemala'].tolist()
        guinea	= countries['guinea'].tolist()
        guinea_bissau	= countries['guinea-bissau'].tolist()
        guyana	= countries['guyana'].tolist()
        haiti	= countries['haiti'].tolist()
        honduras	= countries['honduras'].tolist()
        hungary	= countries['hungary'].tolist()
        iceland	= countries['iceland'].tolist()
        india	= countries['india'].tolist()
        indonesia	= countries['indonesia'].tolist()
        iran	= countries['iran'].tolist()
        iraq	= countries['iraq'].tolist()
        ireland	= countries['ireland'].tolist()
        israel	= countries['israel'].tolist()
        italy	= countries['italy'].tolist()
        ivory_coast	= countries['ivory coast'].tolist()
        jamaica	= countries['jamaica'].tolist()
        japan	= countries['japan'].tolist()
        jordan	= countries['jordan'].tolist()
        kazakhstan	= countries['kazakhstan'].tolist()
        kenya	= countries['kenya'].tolist()
        kiribati	= countries['kiribati'].tolist()
        kuwait	= countries['kuwait'].tolist()
        kyrgyzstan	= countries['kyrgyzstan'].tolist()
        laos	= countries['laos'].tolist()
        latvia	= countries['latvia'].tolist()
        lebanon	= countries['lebanon'].tolist()
        lesotho	= countries['lesotho'].tolist()
        liberia	= countries['liberia'].tolist()
        libya	= countries['libya'].tolist()
        liechtenstein	= countries['liechtenstein'].tolist()
        lithuania	= countries['lithuania'].tolist()
        luxembourg	= countries['luxembourg'].tolist()
        madagascar	= countries['madagascar'].tolist()
        malawi	= countries['malawi'].tolist()
        malaysia	= countries['malaysia'].tolist()
        maldives	= countries['maldives'].tolist()
        mali	= countries['mali'].tolist()
        malta	= countries['malta'].tolist()
        marshall_islands	= countries['marshall islands'].tolist()
        mauritania	= countries['mauritania'].tolist()
        mauritius	= countries['mauritius'].tolist()
        mexico	= countries['mexico'].tolist()
        micronesia	= countries['micronesia'].tolist()
        moldova	= countries['moldova'].tolist()
        monaco	= countries['monaco'].tolist()
        mongolia	= countries['mongolia'].tolist()
        montenegro	= countries['montenegro'].tolist()
        morocco	= countries['morocco'].tolist()
        mozambique	= countries['mozambique'].tolist()
        myanmar	= countries['myanmar'].tolist()
        namibia	= countries['namibia'].tolist()
        nauru	= countries['nauru'].tolist()
        nepal	= countries['nepal'].tolist()
        the_netherlands	= countries['the netherlands'].tolist()
        new_zealand	= countries['new zealand'].tolist()
        nicaragua	= countries['nicaragua'].tolist()
        niger	= countries['niger'].tolist()
        nigeria	= countries['nigeria'].tolist()
        north_korea	= countries['north korea'].tolist()
        north_macedonia	= countries['north macedonia'].tolist()
        norway	= countries['norway'].tolist()
        oman	= countries['oman'].tolist()
        pakistan	= countries['pakistan'].tolist()
        palau	= countries['palau'].tolist()
        palestine	= countries['palestine'].tolist()
        panama	= countries['panama'].tolist()
        papua_new_guinea	= countries['papua new guinea'].tolist()
        paraguay	= countries['paraguay'].tolist()
        peru	= countries['peru'].tolist()
        philippines	= countries['philippines'].tolist()
        poland	= countries['poland'].tolist()
        portugal	= countries['portugal'].tolist()
        qatar	= countries['qatar'].tolist()
        republic_of_the_congo	= countries['republic of the congo'].tolist()
        romania	= countries['romania'].tolist()
        russia	= countries['russia'].tolist()
        rwanda	= countries['rwanda'].tolist()
        saint_kitts_and_nevis	= countries['saint kitts and nevis'].tolist()
        saint_lucia	= countries['saint lucia'].tolist()
        saint_vincent_and_the_grenadines	= countries['saint vincent and the grenadines'].tolist()
        samoa	= countries['samoa'].tolist()
        san_marino	= countries['san marino'].tolist()
        sao_tome_and_principe	= countries['sao tome and principe'].tolist()
        saudi_arabia	= countries['saudi arabia'].tolist()
        senegal	= countries['senegal'].tolist()
        serbia	= countries['serbia'].tolist()
        seychelles	= countries['seychelles'].tolist()
        sierra_leone	= countries['sierra leone'].tolist()
        singapore	= countries['singapore'].tolist()
        slovakia	= countries['slovakia'].tolist()
        slovenia	= countries['slovenia'].tolist()
        solomon_islands	= countries['solomon islands'].tolist()
        somalia	= countries['somalia'].tolist()
        south_africa	= countries['south africa'].tolist()
        south_korea	= countries['south korea'].tolist()
        south_sudan	= countries['south sudan'].tolist()
        spain	= countries['spain'].tolist()
        sri_lanka	= countries['sri lanka'].tolist()
        sudan	= countries['sudan'].tolist()
        suriname	= countries['suriname'].tolist()
        sweden	= countries['sweden'].tolist()
        switzerland	= countries['switzerland'].tolist()
        syria	= countries['syria'].tolist()
        tajikistan	= countries['tajikistan'].tolist()
        tanzania	= countries['tanzania'].tolist()
        thailand	= countries['thailand'].tolist()
        timor_leste	= countries['timor-leste'].tolist()
        togo	= countries['togo'].tolist()
        tonga	= countries['tonga'].tolist()
        trinidad_and_tobago	= countries['trinidad and tobago'].tolist()
        tunisia	= countries['tunisia'].tolist()
        turkey	= countries['turkey'].tolist()
        turkmenistan	= countries['turkmenistan'].tolist()
        tuvalu	= countries['tuvalu'].tolist()
        uganda	= countries['uganda'].tolist()
        ukraine	= countries['ukraine'].tolist()
        united_arab_emirates	= countries['united arab emirates'].tolist()
        united_kingdom	= countries['united kingdom'].tolist()
        united_states_of_america	= countries['united states of america'].tolist()
        uruguay	= countries['uruguay'].tolist()
        uzbekistan	= countries['uzbekistan'].tolist()
        vanuatu	= countries['vanuatu'].tolist()
        vatican_city	= countries['vatican city'].tolist()
        venezuela	= countries['venezuela'].tolist()
        vietnam	= countries['vietnam'].tolist()
        yemen	= countries['yemen'].tolist()
        zambia	= countries['zambia'].tolist()
        zimbabwe	= countries['zimbabwe'].tolist()
        self.countries['afghanistan'] =	afghanistan
        self.countries['albania'] =	albania
        self.countries['algeria'] =	algeria
        self.countries['american samoa'] =	american_samoa
        self.countries['andorra'] =	andorra
        self.countries['angola'] =	angola
        self.countries['antarctica'] =	antarctica
        self.countries['antigua and barbuda'] =	antigua_and_barbuda
        self.countries['argentina'] =	argentina
        self.countries['armenia'] =	armenia
        self.countries['australia'] =	australia
        self.countries['austria'] =	austria
        self.countries['azerbaijan'] =	azerbaijan
        self.countries['bahamas'] =	bahamas
        self.countries['bahrain'] =	bahrain
        self.countries['bangladesh'] =	bangladesh
        self.countries['barbados'] =	barbados
        self.countries['belarus'] =	belarus
        self.countries['belgium'] =	belgium
        self.countries['belize'] =	belize
        self.countries['benin'] =	benin
        self.countries['bhutan'] =	bhutan
        self.countries['bolivia'] =	bolivia
        self.countries['bosnia and herzegovina'] =	bosnia_and_herzegovina
        self.countries['botswana'] =	botswana
        self.countries['brazil'] =	brazil
        self.countries['brunei'] =	brunei
        self.countries['bulgaria'] =	bulgaria
        self.countries['burkina faso'] =	burkina_faso
        self.countries['burundi'] =	burundi
        self.countries['cambodia'] =	cambodia
        self.countries['cameroon'] =	cameroon
        self.countries['canada'] =	canada
        self.countries['cape verde'] =	cape_verde
        self.countries['central african republic'] =	central_african_republic
        self.countries['chad'] =	chad
        self.countries['chile'] =	chile
        self.countries['china'] =	china
        self.countries['colombia'] =	colombia
        self.countries['comoros'] =	comoros
        self.countries['costa rica'] =	costa_rica
        self.countries['croatia'] =	croatia
        self.countries['cuba'] =	cuba
        self.countries['cyprus'] =	cyprus
        self.countries['czech republic'] =	czech_republic
        self.countries['democratic republic of the congo'] =	democratic_republic_of_the_congo
        self.countries['denmark'] =	denmark
        self.countries['djibouti'] =	djibouti
        self.countries['dominica'] =	dominica
        self.countries['dominican republic'] =	dominican_republic
        self.countries['ecuador'] =	ecuador
        self.countries['egypt'] =	egypt
        self.countries['el salvador'] =	el_salvador
        self.countries['equatorial guinea'] =	equatorial_guinea
        self.countries['eritrea'] =	eritrea
        self.countries['estonia'] =	estonia
        self.countries['eswatini'] =	eswatini
        self.countries['ethiopia'] =	ethiopia
        self.countries['fiji'] =	fiji
        self.countries['finland'] =	finland
        self.countries['france'] =	france
        self.countries['gabon'] =	gabon
        self.countries['gambia'] =	gambia
        self.countries['georgia'] =	georgia
        self.countries['germany'] =	germany
        self.countries['ghana'] =	ghana
        self.countries['greece'] =	greece
        self.countries['grenada'] =	grenada
        self.countries['guatemala'] =	guatemala
        self.countries['guinea'] =	guinea
        self.countries['guinea-bissau'] =	guinea_bissau
        self.countries['guyana'] =	guyana
        self.countries['haiti'] =	haiti
        self.countries['honduras'] =	honduras
        self.countries['hungary'] =	hungary
        self.countries['iceland'] =	iceland
        self.countries['india'] =	india
        self.countries['indonesia'] =	indonesia
        self.countries['iran'] =	iran
        self.countries['iraq'] =	iraq
        self.countries['ireland'] =	ireland
        self.countries['israel'] =	israel
        self.countries['italy'] =	italy
        self.countries['ivory coast'] =	ivory_coast
        self.countries['jamaica'] =	jamaica
        self.countries['japan'] =	japan
        self.countries['jordan'] =	jordan
        self.countries['kazakhstan'] =	kazakhstan
        self.countries['kenya'] =	kenya
        self.countries['kiribati'] =	kiribati
        self.countries['kuwait'] =	kuwait
        self.countries['kyrgyzstan'] =	kyrgyzstan
        self.countries['laos'] =	laos
        self.countries['latvia'] =	latvia
        self.countries['lebanon'] =	lebanon
        self.countries['lesotho'] =	lesotho
        self.countries['liberia'] =	liberia
        self.countries['libya'] =	libya
        self.countries['liechtenstein'] =	liechtenstein
        self.countries['lithuania'] =	lithuania
        self.countries['luxembourg'] =	luxembourg
        self.countries['madagascar'] =	madagascar
        self.countries['malawi'] =	malawi
        self.countries['malaysia'] =	malaysia
        self.countries['maldives'] =	maldives
        self.countries['mali'] =	mali
        self.countries['malta'] =	malta
        self.countries['marshall islands'] =	marshall_islands
        self.countries['mauritania'] =	mauritania
        self.countries['mauritius'] =	mauritius
        self.countries['mexico'] =	mexico
        self.countries['micronesia'] =	micronesia
        self.countries['moldova'] =	moldova
        self.countries['monaco'] =	monaco
        self.countries['mongolia'] =	mongolia
        self.countries['montenegro'] =	montenegro
        self.countries['morocco'] =	morocco
        self.countries['mozambique'] =	mozambique
        self.countries['myanmar'] =	myanmar
        self.countries['namibia'] =	namibia
        self.countries['nauru'] =	nauru
        self.countries['nepal'] =	nepal
        self.countries['the netherlands'] =	the_netherlands
        self.countries['new zealand'] =	new_zealand
        self.countries['nicaragua'] =	nicaragua
        self.countries['niger'] =	niger
        self.countries['nigeria'] =	nigeria
        self.countries['north korea'] =	north_korea
        self.countries['north macedonia'] =	north_macedonia
        self.countries['norway'] =	norway
        self.countries['oman'] =	oman
        self.countries['pakistan'] =	pakistan
        self.countries['palau'] =	palau
        self.countries['palestine'] =	palestine
        self.countries['panama'] =	panama
        self.countries['papua new guinea'] =	papua_new_guinea
        self.countries['paraguay'] =	paraguay
        self.countries['peru'] =	peru
        self.countries['philippines'] =	philippines
        self.countries['poland'] =	poland
        self.countries['portugal'] =	portugal
        self.countries['qatar'] =	qatar
        self.countries['republic of the congo'] =	republic_of_the_congo
        self.countries['romania'] =	romania
        self.countries['russia'] =	russia
        self.countries['rwanda'] =	rwanda
        self.countries['saint kitts and nevis'] =	saint_kitts_and_nevis
        self.countries['saint lucia'] =	saint_lucia
        self.countries['saint vincent and the grenadines'] =	saint_vincent_and_the_grenadines
        self.countries['samoa'] =	samoa
        self.countries['san marino'] =	san_marino
        self.countries['sao tome and principe'] =	sao_tome_and_principe
        self.countries['saudi arabia'] =	saudi_arabia
        self.countries['senegal'] =	senegal
        self.countries['serbia'] =	serbia
        self.countries['seychelles'] =	seychelles
        self.countries['sierra leone'] =	sierra_leone
        self.countries['singapore'] =	singapore
        self.countries['slovakia'] =	slovakia
        self.countries['slovenia'] =	slovenia
        self.countries['solomon islands'] =	solomon_islands
        self.countries['somalia'] =	somalia
        self.countries['south africa'] =	south_africa
        self.countries['south korea'] =	south_korea
        self.countries['south sudan'] =	south_sudan
        self.countries['spain'] =	spain
        self.countries['sri lanka'] =	sri_lanka
        self.countries['sudan'] =	sudan
        self.countries['suriname'] =	suriname
        self.countries['sweden'] =	sweden
        self.countries['switzerland'] =	switzerland
        self.countries['syria'] =	syria
        self.countries['tajikistan'] =	tajikistan
        self.countries['tanzania'] =	tanzania
        self.countries['thailand'] =	thailand
        self.countries['timor-leste'] =	timor_leste
        self.countries['togo'] =	togo
        self.countries['tonga'] =	tonga
        self.countries['trinidad and tobago'] =	trinidad_and_tobago
        self.countries['tunisia'] =	tunisia
        self.countries['turkey'] =	turkey
        self.countries['turkmenistan'] =	turkmenistan
        self.countries['tuvalu'] =	tuvalu
        self.countries['uganda'] =	uganda
        self.countries['ukraine'] =	ukraine
        self.countries['united arab emirates'] =	united_arab_emirates
        self.countries['united kingdom'] =	united_kingdom
        self.countries['united states of america'] =	united_states_of_america
        self.countries['uruguay'] =	uruguay
        self.countries['uzbekistan'] =	uzbekistan
        self.countries['vanuatu'] =	vanuatu
        self.countries['vatican city'] =	vatican_city
        self.countries['venezuela'] =	venezuela
        self.countries['vietnam'] =	vietnam
        self.countries['yemen'] =	yemen
        self.countries['zambia'] =	zambia
        self.countries['zimbabwe'] =	zimbabwe

    #Configure countries by continent
    def read_world_countries_by_continent(self):
        print("Configure countries by continent")
        continents = pd.read_excel(r"world_countries_by_continent.xlsx")
        continents.to_csv(r"world_countries_by_continent.csv", sep=",")
        continents = pd.read_csv(r"world_countries_by_continent.csv", sep=",")
        africa	= continents['africa'].tolist()
        antarctica	= continents['antarctica'].tolist()
        asia	= continents['asia'].tolist()
        australia_oceania	= continents['australia/oceania'].tolist()
        europe	= continents['europe'].tolist()
        north_america	= continents['north america'].tolist()
        south_america	= continents['south america'].tolist()
        self.continents['africa'] =	africa
        self.continents['antarctica'] =	antarctica
        self.continents['asia'] =	asia
        self.continents['australia/oceania'] =	australia_oceania
        self.continents['europe'] =	europe
        self.continents['north america'] =	north_america
        self.continents['south america'] =	south_america
