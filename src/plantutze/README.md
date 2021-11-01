# Plantute
source ven/bin/activate
- update genuri.txt
-have fun

## update

UPDATE Specii_ANPM_04 
INNER JOIN completate ON Specii_ANPM_04.Genus = completate.numele 
SET Specii_ANPM_04.increngatura=completate.phylum,
  Specii_ANPM_04.clasa = completate.class,
  Specii_ANPM_04.ordin = completate.order,
  Specii_ANPM_04.familia = completate.family
where Specii_ANPM_04.increngatura is null 
and Specii_ANPM_04.clasa is null 
and Specii_ANPM_04.ordin is null 
and Specii_ANPM_04.familia is null;
