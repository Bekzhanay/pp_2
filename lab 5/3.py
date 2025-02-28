import re
str = "aslifihG_asfadfHKL_SDFJlhf!skjd_fhkJAHFKJAHfskjaFkjnafskjaSNFSKJAHSflkjASKFhALKsfsalksfjlkk"
x = re.findall("[a-z_]+", str)

print(x)