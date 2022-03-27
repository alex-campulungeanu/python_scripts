# Eunis
https://eunis.eea.europa.eu/species.jsp
nohup python -u /app/src/plantutze/eunis/specii.py --user gabriela --file input_1.txt > /app/src/plantutze/eunis/gabriela/output/output_1.log &

# Plantute
source ven/bin/activate
- update genuri.txt

## update

UPDATE Specii_ANPM_10
INNER JOIN completate ON Specii_ANPM_10.Name = completate.numele 
SET Specii_ANPM_10.SPECIA=completate.specia,
  Specii_ANPM_10.AUTOR = completate.autor_specia,
  Specii_ANPM_10.SUBSPECIA = completate.subspecia,
  Specii_ANPM_10.AUTOR_SSP = completate.autor_subspecia,
  Specii_ANPM_10.VARIETATEA = completate.varietatea,
Specii_ANPM_10.AUTOR_VAR = completate.autor_varietatea
where Specii_ANPM_10.SPECIA is null 
and Specii_ANPM_10.AUTOR is null 
and Specii_ANPM_10.SUBSPECIA is null
and Specii_ANPM_10.AUTOR_SSP is null 
and Specii_ANPM_10.VARIETATEA is null
and Specii_ANPM_10.AUTOR_VAR is null;

UPDATE Specii_ANPM_04 
SET gen = genus
where gen is null
and genus is not null;

## TESTE
- Micraspis de 2 ori cu genus
- Mimaeseoptilus  apare cu synonim si cu bare name