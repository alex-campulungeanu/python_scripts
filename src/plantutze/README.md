# Eunis
nohup python -u /app/src/plantutze/eunis/specii.py --user gabriela > /app/src/plantutze/eunis/gabriela/output/output.log &

# Plantute
source ven/bin/activate
- update genuri.txt
-have fun

## update

UPDATE Specii_ANPM_04 
INNER JOIN completate ON Specii_ANPM_04.Genus = completate.numele 
SET Specii_ANPM_04.increngatura=completate.phylum,
  Specii_ANPM_04.clasa = completate.clasa,
  Specii_ANPM_04.ordin = completate.order,
  Specii_ANPM_04.familia = completate.family
where Specii_ANPM_04.increngatura is null 
and Specii_ANPM_04.clasa is null 
and Specii_ANPM_04.ordin is null 
and Specii_ANPM_04.familia is null;

UPDATE Specii_ANPM_04 
SET gen = genus
where gen is null
and genus is not null;

## TESTE
- Micraspis de 2 ori cu genus
- Mimaeseoptilus  apare cu synonim si cu bare name