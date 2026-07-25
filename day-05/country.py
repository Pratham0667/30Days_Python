countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',

];

if len(countries)%2 ==0  :
  middle = countries[len(countries)//2 -1 : len(countries)//2+1]
else :
  middle = countries[len(countries)//2]
print(f"THE MIDDLE COUNTRY : {middle}")


middle_index= (len(countries) + 1) // 2
first_half = countries[:middle_index]
second_half = countries[middle_index:]
print(f"THE FIRST HALF  : \n {first_half}")
print(f"THE SECOND HALF  : \n {second_half}")


country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_con , second_con , third_con  , *scandic = country

print(f" THE FIRST COUNTRY : {first_con} \n THE SECOND COUNTRY : {second_con} \n THE THIRD COUNTRY : { third_con} \n THE REMIAANIG COUNTRY : \n  {scandic}")