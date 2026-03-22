from django.db import models

from doctor.models import doctor
from patient.models import patient

class Proceeding(models.Model):
    id_doctor = models.ForeignKey(doctor.Doctor, on_delete = models.CASCADE)
    id_patient = models.ForeignKey(patient.Patient, on_delete = models.CASCADE)

    class TUSS_CHOICES(models.IntegerChoices):
        CONSULTA_ODONTOLOGICA_INICIAL = 81000057, "81000057 - Consulta Odontológica Inicial"
        CONSULTA_ODONTOLOGICA_DE_URGENCIA = 81000049, "81000049 - Consulta Odontológica de Urgência"
        ATIVIDADE_EDUCATIVA_EM_SAUDE_BUCAL = 82001553, "82001553 - Atividade Educativa em Saúde Bucal"
        CONDICIONAMENTO_EM_ODONTOLOGIA = 82000425, "82000425 - Condicionamento em Odontologia"
        AMPUTACAO_RADICULAR_COM_OBTURACAO_RETROGRADA = 85100021, "85100021 - Amputação Radicular com Obturação Retrógada"
        AMPUTACAO_RADICULAR_SEM_OBTURACAO_RETROGRADA = 85100030, "85100030 - Amputação Radicular sem Obturação Retrógada"
        APICETOMIA_BIRRADICULARES_COM_OBTURACAO_RETROGRADA = 85100048, "85100048 - Apicetomia Birradiculares com Obturação Retrógada"
        APICETOMIA_BIRRADICULARES_SEM_OBTURACAO_RETROGRADA = 85100056, "85100056 - Apicetomia Birradiculares sem Obturação Retrógada"
        APICETOMIA_MULTIRRADICULARES_COM_OBTURACAO_RETROGRADA = 85100064, "85100064 - Apicetomia Multirradiculares com Obturação Retrógada"
        APICETOMIA_MULTIRRADICULARES_SEM_OBTURACAO_RETROGRADA = 85100072, "85100072 - Apicetomia Multirradiculares sem Obturação Retrógada"
        APICETOMIA_UNIRRADICULARES_COM_OBTURACAO_RETROGRADA = 85100080, "85100080 - Apicetomia Unirradiculares com Obturação Retrógada"
        APICETOMIA_UNIRRADICULARES_SEM_OBTURACAO_RETROGRADA = 85100099, "85100099 - Apicetomia Unirradiculares sem Obturação Retrógada"
        APROFUNDAMENTO_AUMENTO_DE_VESTIBULO = 85100102, "85100102 - Aprofundamento/Aumento de Vestíbulo"
        AUMENTO_DE_COROA_CLINICA = 85100110, "85100110 - Aumento de Coroa Clínica"
        BIOPSIA_DE_BOCA = 85100129, "85100129 - Biópsia de Boca"
        BRIDECTOMIA = 85100137, "85100137 - Bridectomia"
        BRIDOTOMIA = 85100145, "85100145 - Bridotomia"
        CAPEAMENTO_PULPAR_DIRETO = 85400017, "85400017 - Capeamento Pulpar Direto - Excluindo Restauração Final"
        CIRURGIA_PARA_EXOSTOSE_MAXILAR = 85100226, "85100226 - Cirurgia para Exostose Maxilar"
        CIRURGIA_PARA_TORUS_MANDIBULAR = 85100234, "85100234 - Cirurgia para Torus Mandibular"
        CIRURGIA_PARA_TORUS_PALATINO = 85100242, "85100242 - Cirurgia para Torus Palatino"
        CIRURGIA_PERIODONTAL_A_RETALHO = 85100250, "85100250 - Cirurgia Periodontal a Retalho"
        COLAGEM_DE_FRAGMENTOS_DENTARIOS = 85400033, "85400033 - Colagem de Fragmentos Dentários"
        COROA_UNITARIA_PROVISORIA_COM_OU_SEM_PINO = 85300012, "85300012 - Coroa Unitária Provisória com ou sem Pino"
        EXERESE_DE_LIPOMA_NA_REGIAO_BUCO_MAXILO_FACIAL = 85100439, "85100439 - Exérese de Lipoma na Região Buco-Maxilo-Facial"
        EXERESE_DE_PEQUENOS_CISTOS_DE_MANDIBULA_MAXILA = 85100455, "85100455 - Exérese de Pequenos Cistos de Mandíbula/Maxila"
        FRENECTOMIA_LABIAL = 85100498, "85100498 - Frenectomia Labial"
        FRENECTOMIA_LINGUAL = 85100501, "85100501 - Frenectomia Lingual"
        FRENOTOMIA_LABIAL = 85100510, "85100510 - Frenotomia Labial"
        FRENOTOMIA_LINGUAL = 85100528, "85100528 - Frenotomia Lingual"
        GENGIVECTOMIA = 85100536, "85100536 - Gengivectomia"
        GENGIVOPLASTIA = 85100544, "85100544 - Gengivoplastia"
        PULPOTOMIA = 85100919, "85100919 - Pulpotomia"
        REABILITACAO_COM_COROA_TOTAL_METALICA_UNITARIA = 85300047, "85300047 - Reabilitação com Coroa Total Metálica Unitária"
        REABILITACAO_COM_NUCLEO_METALICO_FUNDIDO = 85300055, "85300055 - Reabilitação com Núcleo Metálico Fundido/Pré-Fabricado"
        REABILITACAO_COM_RESTAURACAO_METALICA_FUNDIDA_UNITARIA = 85300063, "85300063 - Reabilitação com Restauração Metálica Fundida (RMF) Unitária"
        RECIMENTACAO_DE_PECA_TRABALHO_PROTETICO = 85300071, "85300071 - Recimentação de Peça/Trabalho Protético"
        RECONSTRUCAO_DE_SULCO_GENGIVO_LABIAL = 85100935, "85100935 - Reconstrução de Sulco Gengivo-Labial"
        REDUCAO_CRUENTA_DE_FRATURA_ALVEOLO_DENTARIA = 85100943, "85100943 - Redução Cruenta de Fratura Alvéolo Dentária"
        REDUCAO_INCRUENTA_DE_FRATURA_ALVEOLO_DENTARIA = 85100951, "85100951 - Redução Incruenta de Fratura Alvéolo Dentária"
        REIMPLANTE_DE_DENTE_AVULSIONADO_COM_CONTENCAO = 85100960, "85100960 - Reimplante de Dente Avulsionado com Contenção"
        REMOCAO_DE_CORPO_ESTRANHO_INTRACANAL = 85400157, "85400157 - Remoção de Corpo Estranho Intracanal"
        REMOCAO_DE_DENTES_INCLUSOS_IMPACTADOS = 85100978, "85100978 - Remoção de Dentes Inclusos / Impactados"
        REMOCAO_DE_DENTES_SEMI_INCLUSOS_IMPACTADOS = 85100986, "85100986 - Remoção de Dentes Semi-Inclusos / Impactados"
        REMOCAO_DE_FATORES_DE_RETENCAO_DE_BIOFILME_DENTAL = 82001430, "82001430 - Remoção de Fatores de Retenção de Biofilme Dental"
        REMOCAO_DE_NUCLEO_INTRACANAL = 85400165, "85400165 - Remoção de Núcleo Intracanal"
        REMOCAO_DE_PECA_TRABALHO_PROTETICO = 85300080, "85300080 - Remoção de Peça/Trabalho Protético"
        RESTAURACAO_EM_AMALGAMA = 85400173, "85400173 - Restauração em Amálgama"
        RESTAURACAO_EM_IONOMERO_DE_VIDRO = 85400190, "85400190 - Restauração em Ionômero de Vidro"
        RESTAURACAO_EM_RESINA_FOTOPOLIMERIZAVEL = 85400211, "85400211 - Restauração em Resina Fotopolimerizável"
        TRATAMENTO_DE_ABSCESSO_PERIODONTAL = 85101010, "85101010 - Tratamento de Abscesso Periodontal"
        TRATAMENTO_DE_ALVEOLITE = 85101028, "85101028 - Tratamento de Alveolite"
        TRATAMENTO_DE_ODONTALGIA_AGUDA = 85101044, "85101044 - Tratamento de Odontalagia Aguda"
        TRATAMENTO_ENDODONTICO_BIRRADICULAR = 85400505, "85400505 - Tratamento Endodôntico Birradicular"
        TRATAMENTO_ENDODONTICO_MULTIRRADICULAR = 85400513, "85400513 - Tratamento Endodôntico Multirradicular"
        TRATAMENTO_ENDODONTICO_UNIRRADICULAR = 85400521, "85400521 - Tratamento Endodôntico Unirradicular"
        ULECTOMIA = 85101079, "85101079 - Ulectomia"
        ULOTOMIA = 85101087, "85101087 - Ulotomia"
    
    tuss_code = models.IntegerField(
        blank = False,
        choices=TUSS_CHOICES.choices
    )
    date = models.DateTimeField(auto_now_add = True)
    
    class ProceedingType(models.TextChoices):
        INQUIRY = 'Inquiry', 'Consulta'
        PROCEEDING = 'Proceeding', 'Procedimento'
    
    description = models.TextField()

    proceeding_type = models.CharField(
        max_length=20,
        choices=ProceedingType.choices,
        default=ProceedingType.PROCEEDING
    )


    def __str__(self):
        return f"{self.date}: {self.id_patient}"

