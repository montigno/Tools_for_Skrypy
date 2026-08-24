import json


# --------------------------------------------------
# Lecture du fichier JSON
# --------------------------------------------------

with open("nipype_interfaces.json", "r", encoding="utf-8") as f:
    data = json.load(f)


# --------------------------------------------------
# Affichage d'une interface
# --------------------------------------------------

def afficher_interface(nom, info, indentation=""):

    print(f"{indentation}{'=' * 70}")
    print(f"{indentation}INTERFACE : {nom}")
    print(f"{indentation}MODULE    : {info.get('module', '')}")
    print(f"{indentation}{'=' * 70}")

    # ----------------------------------------------
    # INPUTS
    # ----------------------------------------------

    print(f"\n{indentation}  INPUTS")

    inputs = info.get("inputs", {})

    if not inputs:
        print(f"{indentation}    Aucun input")

    for input_name, input_info in inputs.items():

        print(f"\n{indentation}    {input_name}")

        print(
            f"{indentation}      type      : "
            f"{input_info.get('type')}"
        )

        print(
            f"{indentation}      default   : "
            f"{input_info.get('default')}"
        )

        print(
            f"{indentation}      mandatory : "
            f"{input_info.get('mandatory')}"
        )

        if "xor" in input_info:
            print(
                f"{indentation}      xor       : "
                f"{input_info['xor']}"
            )

        # ------------------------------------------
        # ENUM
        # ------------------------------------------

        if input_info.get("type") == "Enum":

            structure = input_info.get("structure", {})

            values = structure.get("values", [])

            print(
                f"{indentation}      values    : "
                f"{values}"
            )

    # ----------------------------------------------
    # OUTPUTS
    # ----------------------------------------------

    print(f"\n{indentation}  OUTPUTS")

    outputs = info.get("outputs", {})

    if not outputs:
        print(f"{indentation}    Aucun output")

    for output_name, output_info in outputs.items():

        print(f"\n{indentation}    {output_name}")

        print(
            f"{indentation}      type      : "
            f"{output_info.get('type')}"
        )

        print(
            f"{indentation}      default   : "
            f"{output_info.get('default')}"
        )

        print(
            f"{indentation}      mandatory : "
            f"{output_info.get('mandatory')}"
        )

        if "xor" in output_info:
            print(
                f"{indentation}      xor       : "
                f"{output_info['xor']}"
            )

        # ------------------------------------------
        # ENUM
        # ------------------------------------------

        if output_info.get("type") == "Enum":

            structure = output_info.get("structure", {})

            values = structure.get("values", [])

            print(
                f"{indentation}      values    : "
                f"{values}"
            )


# --------------------------------------------------
# Parcours récursif des modules
# --------------------------------------------------

def parcourir_module(nom_module, contenu, niveau=0):

    indentation = "    " * niveau

    print("\n")
    print(f"{indentation}{'#' * 70}")
    print(f"{indentation}MODULE : {nom_module}")
    print(f"{indentation}{'#' * 70}")

    # ----------------------------------------------
    # Interfaces du module courant
    # ----------------------------------------------

    interfaces = contenu.get("interfaces", {})

    for nom_interface, info_interface in interfaces.items():

        afficher_interface(
            nom_interface,
            info_interface,
            indentation + "  "
        )

    # ----------------------------------------------
    # Sous-modules
    # ----------------------------------------------

    for nom, valeur in contenu.items():

        if nom == "interfaces":
            continue

        if isinstance(valeur, dict):

            parcourir_module(
                nom,
                valeur,
                niveau + 1
            )


def afficher_parametre(nom, info, indentation=""):

    print(f"{indentation}{nom}")

    print(
        f"{indentation}  type      : "
        f"{info.get('type')}"
    )

    print(
        f"{indentation}  default   : "
        f"{info.get('default')}"
    )

    print(
        f"{indentation}  mandatory : "
        f"{info.get('mandatory')}"
    )

    if info.get("xor"):
        print(
            f"{indentation}  xor       : "
            f"{info['xor']}"
        )

    if info.get("type") == "Enum":

        values = info.get(
            "structure", {}
        ).get(
            "values",
            []
        )

        print(
            f"{indentation}  values    : "
            f"{values}"
        )
        
    if info.get("type") == "List":
        
        values = info.get(
            "structure", {}
        ).get(
            "element",
            {}
        ).get(
            "elements",
            []
        )

        print(
            f"{indentation}  elements    : "
            f"{values}"
        )

    if info.get("type") == "TraitCompound":
            
            values = info.get(
                "structure", {}
            ).get(
                "types",
                {}
            )
    
            print(
                f"{indentation}  types    : "
                f"{values}"
            )       
        

# --------------------------------------------------
# Recherche et affichage de AFNI
# --------------------------------------------------

if "afni" in data:

    print("\n")
    print("=" * 80)
    print("NIPYPE AFNI")
    print("=" * 80)

    # parcourir_module(
    #     "afni",
    #     data["afni"]
    # )
    
    inputs = data["afni"]["preprocess"]["interfaces"]["AlignEpiAnatPy"]["inputs"]
    
    for input_name, input_info in inputs.items():

        afficher_parametre(
            input_name,
            input_info
        )

else:

    print("Le module 'afni' n'a pas été trouvé dans le JSON.")