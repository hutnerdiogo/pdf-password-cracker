import PyPDF2

# Put the file name/directory
file = "pdf with password.pdf"


def testar_senha(senha):
    try:
        with open(file, 'rb') as arquivo_pdf:

            leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
            print('Testing...')
            # Verificando se o arquivo está criptografado
            if leitor_pdf.is_encrypted:
                # Tentando descriptografar com a senha fornecida
                if leitor_pdf.decrypt(senha):
                    return True
                else:
                    return False
            else:
                return False
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file}")
        return True
    except Exception as e:
        print(str(e))
        return True


# Put the amount of digits in the password
password_digits_amount = 5
for i in range(10 ** password_digits_amount):
    palpite = str(i).zfill(password_digits_amount)
    print(palpite)

    resultado = testar_senha(palpite)
    if resultado:
        print(f"Password Finder: {palpite}")
        break
