# Ruta de la clave PGP utilizada para cifrar y descifrar el archivo
SOPS_KEY_PATH=/pgp/sops_functional_tests_key.asc

# Nombre del archivo de secretos original y su versión cifrada
SECRET_FILE=secrets.yaml
ENCRYPTED_FILE=secrets.enc.yaml

# Cifrar el archivo secrets.yaml usando SOPS
encrypt:
	sops -e --pgp $(SOPS_KEY_PATH) $(SECRET_FILE) > $(ENCRYPTED_FILE)
	@echo "El archivo $(SECRET_FILE) ha sido cifrado y guardado como $(ENCRYPTED_FILE)."

# Descifrar el archivo secrets.enc.yaml usando SOPS
decrypt:
	sops -d $(ENCRYPTED_FILE) > $(SECRET_FILE)
	@echo "El archivo $(ENCRYPTED_FILE) ha sido descifrado y guardado como $(SECRET_FILE)."

# Requiere tener `make` instalado en el sistema.
