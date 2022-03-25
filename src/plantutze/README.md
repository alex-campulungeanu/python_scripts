# Eunis
https://eunis.eea.europa.eu/species.jsp
nohup python -u /app/src/plantutze/eunis/specii.py --user gabriela --file input_1.txt > /app/src/plantutze/eunis/gabriela/output/output_1.log &

# Plantute
source ven/bin/activate
- update genuri.txt
-have fun

## update

UPDATE Specii_ANPM_08 
INNER JOIN completate ON Specii_ANPM_08.Name = completate.numele 
SET Specii_ANPM_08.SPECIA=completate.specia,
  Specii_ANPM_08.AUTOR = completate.autorul,
  Specii_ANPM_08.SUBSPECIA = completate.subspecia,
  Specii_ANPM_08.VARIETATEA = completate.varietatea
where Specii_ANPM_08.SPECIA is null 
and Specii_ANPM_08.AUTOR is null 
and Specii_ANPM_08.SUBSPECIA is null 
and Specii_ANPM_08.VARIETATEA is null;

UPDATE Specii_ANPM_04 
SET gen = genus
where gen is null
and genus is not null;

## TESTE
- Micraspis de 2 ori cu genus
- Mimaeseoptilus  apare cu synonim si cu bare name