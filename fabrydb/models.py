# -*- coding: latin-1 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
#
# Feel free to rename the models, but don't rename db_table values or field
# names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom
# [appname]' into your database.

from __future__ import unicode_literals

from django.db import models
import datetime
from django.db.models import Sum

DEFAULT_VALUES = {
    'default_simnao': 'Desconhecido',
    'verbose_id': 'Paciente'
}

SIMNAO_CHOICES = (('Desconhecido', 'Desconhecido'), ('Sim', 'Sim'),
                  ('Não', 'Não'), ('Não divulgado', 'Não divulgado'))


def format_datefield(my_field):
    if not my_field:
        return 'Data Desconhecida'
    else:
        return my_field.strftime('%Y-%m-%d')


class Tiposecg(models.Model):
    id_tiposecg = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposecg'


class TiposecocardiogramaI(models.Model):
    id_tiposecocardiograma_i = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposecocardiograma_i'


class Tiposholter2H(models.Model):
    id_tiposholter2h = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposholter2h'


class AvaliacaoCardiologica(models.Model):
    id = models.ForeignKey('Dadosgerais', db_column='id',
                           verbose_name=DEFAULT_VALUES['verbose_id'])
    id_avaliacaocardiologica = models.AutoField(primary_key=True)
    data = models.DateField(null=True, blank=True)
    holter2h = models.CharField(max_length=50, blank=True)
    ecocardiograma_i = models.TextField(blank=True)
    ecocardiograma_ii_diametros_estruturais_mm = \
        models.IntegerField(null=True, blank=True)
    aorta_diametro_da_raiz_mm = models.IntegerField(null=True, blank=True)
    atrio_esquerdo_mm = models.IntegerField(null=True, blank=True)
    diametro_ventricular_direito_mm = models.IntegerField(null=True,
                                                          blank=True)
    diametro_diastolico_final_do_ve_mm = models.IntegerField(null=True,
                                                             blank=True)
    espessura_diatolica_do_septo_mm = models.IntegerField(null=True,
                                                          blank=True)
    espessura_diatolica_da_ppve_mm = models.IntegerField(null=True, blank=True)
    relacao_atrio_esquerdoaorta_ecocardiograma_iii =\
        models.FloatField(null=True, blank=True)
    fracao_de_ejecao_teicholz = models.FloatField(null=True, blank=True)
    massa_ventricular_esquerda_g = models.IntegerField(null=True, blank=True)
    relacao_massasuperficie_corporal_gm2 = models.FloatField(null=True,
                                                             blank=True)
    percent_encurt_cavidade = models.FloatField(null=True, blank=True)
    relacao_septoppve = models.FloatField(null=True, blank=True)
    volume_diatolico_final_ml = models.IntegerField(null=True, blank=True)
    volume_sistolico_ml = models.IntegerField(null=True, blank=True)
    relacao_volume_massa_mlg = models.FloatField(null=True, blank=True)
    volume_sistolico_final_ml = models.IntegerField(null=True, blank=True)
    palpitacoes = models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                                   default='Desconhecido')
    angina = models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                              default='Desconhecido')
    ecg = models.CharField(max_length=50, blank=True)
    category_ecg = models.ManyToManyField(Tiposecg,
                                          through='AvaliacaoCardiologicaecg')
    category_ecocardiogramai = models.ManyToManyField(
        TiposecocardiogramaI, through='AvaliacaoCardiologicaecocardiogramaI')
    category_holter2h = models.ManyToManyField(
        Tiposholter2H, through='AvaliacaoCardiologicaholter2H')

    def __unicode__(self):
        return "{0}, {1}".format(self.id, format_datefield(self.data))

    class Meta:
        db_table = 'avaliacao_cardiologica'


class AvaliacaoCardiologicaecg(models.Model):
    id_avaliacao_cardiologicaecg = models.AutoField(primary_key=True)
    id_avaliacaocardiologica = \
        models.ForeignKey(AvaliacaoCardiologica,
                          db_column='id_avaliacaocardiologica')
    id_tiposecg = models.ForeignKey('Tiposecg', db_column='id_tiposecg')

    def __unicode__(self):
        return "{0}".format("Categoria de ECG")

    class Meta:
        db_table = 'avaliacao_cardiologicaecg'


class AvaliacaoCardiologicaecocardiogramaI(models.Model):
    id_avaliacao_cardiologicaecocardiograma_i = \
        models.AutoField(primary_key=True)
    id_avaliacaocardiologica = \
        models.ForeignKey(AvaliacaoCardiologica,
                          db_column='id_avaliacaocardiologica')
    id_tiposecocardiograma_i = \
        models.ForeignKey('TiposecocardiogramaI',
                          db_column='id_tiposecocardiograma_i')

    class Meta:
        db_table = 'avaliacao_cardiologicaecocardiograma_i'


class AvaliacaoCardiologicaholter2H(models.Model):
    id_avaliacao_cardiologicaholter2h = models.AutoField(primary_key=True)
    id_avaliacaocardiologica = models.ForeignKey(
        AvaliacaoCardiologica, db_column='id_avaliacaocardiologica')
    id_tiposholter2h = models.ForeignKey(
        'Tiposholter2H', db_column='id_tiposholter2h')

    class Meta:
        db_table = 'avaliacao_cardiologicaholter2h'


class AvaliacaoNeurologica(models.Model):
    id = models.ForeignKey('Dadosgerais', db_column='id',
                           verbose_name=DEFAULT_VALUES['verbose_id'])
    id_neurologica = models.AutoField(primary_key=True)
    data = models.DateField(null=True, blank=True)
    ressonancia_magnetica = models.TextField(blank=True)
    angioressonancia_magnetica = models.CharField(max_length=200, blank=True)
    outros_dados = models.CharField(max_length=200, blank=True)
    category_angioressonancia_magnetica =\
        models.ForeignKey('TiposangioressonanciaMagnetica',
                          db_column='category_angioressonancia_magnetica')

    def __unicode__(self):
        return "{0}, {1}".format(self.id, format_datefield(self.data))

    class Meta:
        db_table = 'avaliacao_neurologica'


class AvaliacaoOftalmologica(models.Model):
    id = models.ForeignKey('Dadosgerais', db_column='id',
                           verbose_name=DEFAULT_VALUES['verbose_id'])
    id_oftalmologia = models.AutoField(primary_key=True)
    data = models.DateField(null=True, blank=True)
    cornea_verticilata = models.CharField(max_length=20,
                                          choices=SIMNAO_CHOICES,
                                          default='Desconhecido')
    tortuosidade_dos_vasos_retinianos = \
        models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                         default='Desconhecido')
    tortuosidade_dos_vasos_conjuntivais = \
        models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                         default='Desconhecido')
    opacidade_da_cornea = models.CharField(max_length=20,
                                           choices=SIMNAO_CHOICES,
                                           default='Desconhecido')
    campo_para_upload_de_fotos = models.TextField(blank=True)
    outros_dados = models.CharField(max_length=100, blank=True)
    outros_exames_relevantes = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return "{0}, {1}".format(self.id, format_datefield(self.data))

    class Meta:
        db_table = 'avaliacao_oftalmologica'


class TiposresultadoDaBiopsia(models.Model):
    id_tiposresultado_da_biopsia = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposresultado_da_biopsia'


class AvaliacaoRenal(models.Model):
    id = models.ForeignKey('Dadosgerais', db_column='id',
                           verbose_name=DEFAULT_VALUES['verbose_id'])
    id_renal = models.AutoField(primary_key=True)
    data = models.DateField(null=True, blank=True)
    eas = models.CharField(max_length=255, blank=True)
    creatinina_serica_mgdl = models.FloatField(null=True, blank=True)
    creatinina_urinaria1_mgdl = models.FloatField(null=True, blank=True)
    creatinina_urinaria2_mgdl = models.FloatField(null=True, blank=True)
    creatinina_urinaria3_mgdl = models.FloatField(null=True, blank=True)
    ureia_mgdl = models.FloatField(null=True, blank=True)
    albumina_mgdl = models.FloatField(null=True, blank=True)
    microalbuminuria1_microgmin = models.FloatField(null=True, blank=True)
    microalbuminuria2_microgmin = models.FloatField(null=True, blank=True)
    microalbuminuria3_microgmin = models.FloatField(null=True, blank=True)
    volume_urinario_ml = models.IntegerField(null=True, blank=True)
    cistatina_c_mgl = models.FloatField(null=True, blank=True)
    altura_cm = models.FloatField(null=True, blank=True)
    peso_kg = models.FloatField(null=True, blank=True)
    ritmo_de_filtracao_glomerular_estimado = models.FloatField(null=True,
                                                               blank=True)
    cockcroft_gault = models.FloatField(null=True, blank=True)
    schwartz = models.FloatField(null=True, blank=True)
    proteinuria1_mgdl = models.FloatField(null=True, blank=True)
    proteinuria2_mgdl = models.FloatField(null=True, blank=True)
    proteinuria3_mgdl = models.FloatField(null=True, blank=True)
    biopsia_renal = models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                                     default='Desconhecido')
    resultado_da_biopsia = models.CharField(max_length=255, blank=True)
    fotos_da_biopsia = models.TextField(blank=True)
    outros = models.CharField(max_length=255, blank=True)
    category_resultados_da_biopsia = \
        models.ManyToManyField(TiposresultadoDaBiopsia,
                               through='AvaliacaoRenalresultadoDaBiopsia')

    def __unicode__(self):
        return "{0}, {1}".format(self.id, format_datefield(self.data))

    class Meta:
        db_table = 'avaliacao_renal'


class AvaliacaoRenalresultadoDaBiopsia(models.Model):
    id_avaliacao_renalresultado_da_biopsia = \
        models.AutoField(primary_key=True)
    id_renal = models.ForeignKey(AvaliacaoRenal, db_column='id_renal')
    id_tiposresultado_da_biopsia = \
        models.ForeignKey('TiposresultadoDaBiopsia',
                          db_column='id_tiposresultado_da_biopsia')

    class Meta:
        db_table = 'avaliacao_renalresultado_da_biopsia'


class Banco(models.Model):
    id = models.ForeignKey('Dadosgerais', db_column='id',
                           verbose_name=DEFAULT_VALUES['verbose_id'])
    id_banco = models.IntegerField(primary_key=True)
    papel_de_filtro_data_coleta = models.DateField(null=True, blank=True)
    papel_de_filtro_data_envio = models.DateField(null=True, blank=True)
    papel_de_filtro_destinatario = models.CharField(max_length=255, blank=True)
    dna_data_coleta = models.DateField(null=True, blank=True)
    dna_data_envio = models.DateField(null=True, blank=True)
    dna_destinatario = models.CharField(max_length=255, blank=True)
    sangue_data_coleta = models.DateField(null=True, blank=True)
    sangue_data_envio = models.DateField(null=True, blank=True)
    sangue_destinatario = models.CharField(max_length=255, blank=True)
    urina_data_coleta = models.DateField(null=True, blank=True)
    urina_data_envio = models.DateField(null=True, blank=True)
    urina_destinatario = models.CharField(max_length=255, blank=True)
    plasma_data_coleta = models.DateField(null=True, blank=True)
    plasma_data_envio = models.DateField(null=True, blank=True)
    plasma_destinatario = models.CharField(max_length=255, blank=True)
    soro_data_coleta = models.DateField(null=True, blank=True)
    soro_data_envio = models.DateField(null=True, blank=True)
    soro_destinatario = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return "{0}".format(self.id)

    class Meta:
        db_table = 'banco'


class BioquimicaGeral(models.Model):
    id = models.ForeignKey('Dadosgerais', db_column='id',
                           verbose_name=DEFAULT_VALUES['verbose_id'])
    id_bioquimica = models.AutoField(primary_key=True)
    data = models.DateField(null=True, blank=True)
    hemoglobina_gdl = models.FloatField(null=True, blank=True)
    hematocrito = models.FloatField(null=True, blank=True)
    leucograma_mm3 = models.IntegerField(null=True, blank=True)
    plaquetas_mm3 = models.IntegerField(null=True, blank=True)
    na = models.FloatField(null=True, blank=True)
    k = models.FloatField(null=True, blank=True)
    ca = models.FloatField(null=True, blank=True)
    fosfato = models.FloatField(null=True, blank=True)
    mg = models.FloatField(null=True, blank=True)
    cl = models.FloatField(null=True, blank=True)
    ast = models.IntegerField(null=True, blank=True)
    alt = models.IntegerField(null=True, blank=True)
    proteinas_totais = models.FloatField(null=True, blank=True)
    albuminas = models.FloatField(null=True, blank=True)
    globulinas = models.FloatField(null=True, blank=True)
    relacao_albumina_globulina_pq = models.FloatField(null=True, blank=True)
    colesterol_total_mgdl = models.IntegerField(null=True, blank=True)
    colesterol_hdl_mgdl = models.IntegerField(null=True, blank=True)
    triglicerideos_mgdl = models.IntegerField(null=True, blank=True)
    colesterol_ldl_mgdl = models.IntegerField(null=True, blank=True)
    colesterol_vldl_mgdl = models.IntegerField(null=True, blank=True)
    lyso_gb3 = models.CharField(max_length=255, blank=True)
    gb3_urinario = models.CharField(max_length=255, blank=True)
    ipk = models.CharField(max_length=255, blank=True)
    cd77 = models.CharField(max_length=255, blank=True)
    homocisteina = models.IntegerField(null=True, blank=True)
    igg = models.CharField(max_length=20, default='0')
    ige = models.CharField(max_length=20, default='0')
    imunoeletrofoesses_de_proteinas = models.TextField(blank=True)

    def __unicode__(self):
        return "{0}, {1}".format(self.id, format_datefield(self.data))

    class Meta:
        db_table = 'bioquimica_geral'


class Classes(models.Model):
    codigo = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'classes'


class DadosDaInfusao(models.Model):
    id = models.ForeignKey('Dadosgerais', db_column='id',
                           verbose_name=DEFAULT_VALUES['verbose_id'])
    id_infusao = models.AutoField(primary_key=True)
    data = models.DateField(null=True, blank=True,
                            default=datetime.date.today())
    lote = models.CharField(max_length=20)

    _numero_da_infusao = models.IntegerField(null=True, blank=True, db_column='numero_da_infusao')

    @property
    def numero_da_infusao(self):
        if not self.data: return -1
        return len(DadosDaInfusao.objects.filter(id__id = self.id_id, data__lte = self.data))

    @numero_da_infusao.setter
    def numero_de_infusoo(self):
        self._numero_da_infusao = value

    anamnese = models.CharField(max_length=250, blank=True)
    exame_fisico = models.CharField(max_length=250, blank=True)
    fc_bpm_pre_infusional = models.IntegerField(null=True, blank=True)
    fr_irpm_pre_infusional = models.IntegerField(null=True, blank=True)
    pa_mmhg_pre_infusional = models.CharField(max_length=8, blank=True)
    tax_celsius_pre_infusional = models.FloatField(null=True, blank=True)
    altura_m = models.FloatField(null=True, blank=True, db_column='altura_m')

    _peso_kg = models.FloatField(null=True, db_column='peso_kg')

    @property
    def peso_kg(self):
        return self._peso_kg

    @peso_kg.setter
    def peso_kg(self, value):
        self._peso_kg = value

    _posologia_administrada_ml = models.FloatField(null=True, blank=True, db_column='posologia_administrada_ml')

    @property
    def posologia_administrada_ml(self):
        return self._peso_kg * 0.2

    @posologia_administrada_ml.setter
    def posologia_administrada_ml(self):
        self._posologia_administrada_ml = value

    @property
    def dose_accumulada(self):
        if not self.data: return -1
        l = DadosDaInfusao.objects.filter(id_id = self.id_id, data__lte = self.data)
        return sum([d.posologia_administrada_ml for d in l])

    @property
    def numero_de_infusoes_no_mes(self):
        if not self.data: return -1
        l = DadosDaInfusao.objects.filter(
            id_id = self.id_id,
            data__range = [self.data - datetime.timedelta(days=30), self.data])
        return len(l)

    fc_bpm_pos_infusional = models.IntegerField(null=True, blank=True)
    fr_irpm_pos_infusional = models.IntegerField(null=True, blank=True)
    pa_mmhg_pos_infusional = models.CharField(max_length=8, blank=True)
    tax_celsius_pos_infusional = models.FloatField(null=True, blank=True)
    conduta_a_reacao_pos_infusao = models.CharField(max_length=100, blank=True)
    reacao_pos_infusao = models.CharField(max_length=20,
                                          choices=SIMNAO_CHOICES,
                                          default='Desconhecido')
    category_reacao_pos_infusao = \
        models.ForeignKey('TiposreacaoPosInfusao', null=True,
                          db_column='category_reacao_pos_infusao', blank=True)
    category_conduta_a_reacao_pos_infusao = \
        models.ForeignKey('TiposcondutaAReacaoPosInfusao', null=True,
                          db_column='category_conduta_a_reacao_pos_infusao',
                          blank=True)

    def save(self, *args, **kwargs):
        self._posologia_administrada_ml = self.posologia_administrada_ml
        self._numero_da_infusao = self.numero_da_infusao
        super(DadosDaInfusao, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        return "{0}, {1}".format(self.id, format_datefield(self.data))

    class Meta:
        db_table = 'dados_da_infusao'


class TiposmedicacoesEmUso(models.Model):
    id_tiposmedicacoes_em_uso = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposmedicacoes_em_uso'


class Dadosgerais(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=15, blank=True)
    nome = models.CharField(max_length=100)
    data_de_nascimento = models.DateField()
    idade_anos = models.IntegerField(null=True, blank=True)
    logradouro = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=5, blank=True)
    complemento = models.CharField(max_length=20, blank=True)
    bairro = models.CharField(max_length=40, blank=True)
    municipio = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    cep = models.CharField(max_length=11, blank=True)
    data_do_diagnostico = models.DateField(null=True, blank=True)
    idade_ao_diagnostico = models.IntegerField(null=True, blank=True)
    idade_de_inicio_das_manifestacoes_clinicas = models.IntegerField(
        null=True, blank=True)
    genotipagem = models.CharField(max_length=100, blank=True)
    dosagem_enzimatica = models.FloatField(null=True, blank=True)
    gb_3_urinario = models.FloatField(null=True, blank=True)
    medicacoes_em_uso = models.TextField(blank=True)
    fumante = models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                               default='Desconhecido')
    quantidadedia = models.IntegerField(null=True, blank=True)
    alcoolismo = models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                                  default='Desconhecido')
    historia_obstetrica_gera = models.SmallIntegerField(null=True, blank=True)
    historia_obstetrica_para = models.SmallIntegerField(null=True, blank=True)
    historia_obstetrica_aborto = models.SmallIntegerField(null=True,
                                                          blank=True)
    historia_neonatal_condicao_de_nascimento = models.IntegerField(null=True,
                                                                   blank=True)
    historia_neonatal_descricao = models.CharField(max_length=150, blank=True)
    foto = models.TextField(blank=True)
    heredograma = models.TextField(blank=True)
    etnia = models.ForeignKey('Etnia', db_column='etnia')
    sexo = models.ForeignKey('Tipossexo', db_column='sexo')
    category_genotipagem = models.ForeignKey('Tiposgenotipagem',
                                             db_column='category_genotipagem')
    category_medicacoes_em_uso = models.ManyToManyField(
        TiposmedicacoesEmUso, through='DadosgeraismedicacoesEmUso')

    def __unicode__(self):
        return "{0}".format(self.nome)

    class Meta:
        db_table = 'dadosgerais'
        ordering = ['nome', ]


class DadosgeraismedicacoesEmUso(models.Model):
    id_dadosgeraismedicacoes_em_uso = models.AutoField(primary_key=True)
    id = models.ForeignKey(Dadosgerais, db_column='id')
    id_tiposmedicacoes_em_uso = \
        models.ForeignKey('TiposmedicacoesEmUso',
                          db_column='id_tiposmedicacoes_em_uso')

    class Meta:
        db_table = 'dadosgeraismedicacoes_em_uso'


class Etnia(models.Model):
    codigo = models.IntegerField(primary_key=True)
    etnia = models.CharField(max_length=20)
    peso = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return "{0}".format(self.etnia)

    class Meta:
        db_table = 'etnia'


class MssiCardiologico(models.Model):
    id = models.ForeignKey(Dadosgerais, db_column='id',
                           verbose_name=DEFAULT_VALUES['verbose_id'])
    id_mssi_cardiologico = models.AutoField(primary_key=True)
    data = models.DateField(null=True, blank=True)
    modificacoes_na_espessura_do_miocardio = \
        models.ForeignKey('Tiposmodificacoesnaespessuramiocardio',
                          db_column='modificacoes_na_espessura_do_miocardio',
                          verbose_name='Categoria de modificacoes na \
                          espessura do miocardio')
    insuficiencia_valvar = models.CharField(max_length=20,
                                            choices=SIMNAO_CHOICES,
                                            default='Desconhecido')
    anormalidades_no_ecg = models.CharField(max_length=20,
                                            choices=SIMNAO_CHOICES,
                                            default='Desconhecido')
    marcapasso = models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                                  default='Desconhecido')
    hipertensao = models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                                   default='Desconhecido')

    def __unicode__(self):
        return "{0}, {1}".format(self.id, format_datefield(self.data))

    class Meta:
        db_table = 'mssi_cardiologico'


class MssiGeral(models.Model):
    id = models.ForeignKey(Dadosgerais, db_column='id',
                           verbose_name=DEFAULT_VALUES['verbose_id'])
    id_missi_geral = models.AutoField(primary_key=True)
    data = models.DateField(null=True, blank=True)
    aparencia_facial_caracteristica = models.CharField(max_length=20,
                                                       choices=SIMNAO_CHOICES,
                                                       default='Desconhecido')
    angioqueratoma = models.CharField(max_length=8, blank=True)
    edema = models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                             default='Desconhecido')
    musculoesqueletico = models.CharField(max_length=20,
                                          choices=SIMNAO_CHOICES,
                                          default='Desconhecido')
    cornea_verticilata = models.CharField(max_length=20,
                                          choices=SIMNAO_CHOICES,
                                          default='Desconhecido')
    diaforese = models.CharField(max_length=10, blank=True)
    dor_abdominal = models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                                     default='Desconhecido')
    diarreiaconstipacao = models.CharField(max_length=20, blank=True)
    hemorroidas = models.CharField(max_length=20, blank=True)
    pulmonar = models.CharField(max_length=20, blank=True)
    nyha = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return "{0}, {1}".format(self.id, format_datefield(self.data))

    class Meta:
        db_table = 'mssi_geral'


class MssiNeurologicoPsiquiatrico(models.Model):
    id = models.ForeignKey(Dadosgerais, db_column='id',
                           verbose_name=DEFAULT_VALUES['verbose_id'])
    id_mssi_neurologico_psicologico = models.AutoField(primary_key=True)
    data = models.DateField(null=True, blank=True)
    zumbidotinido = models.CharField(max_length=8, blank=True)
    vertigem = models.ForeignKey('Tiposvertigem', db_column='vertigem')
    acroparestesia = models.ForeignKey('Tiposacroparestesia',
                                       db_column='acroparestesia')
    crises_de_febre_e_dor = models.CharField(max_length=20,
                                             choices=SIMNAO_CHOICES,
                                             default='Desconhecido')
    cerebrovascular = models.ForeignKey('Tiposcerebrovascular',
                                        db_column='cerebrovascular')
    depressao = models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                                 default='Desconhecido')
    fadiga = models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                              default='Desconhecido')
    hipoatividade = models.CharField(max_length=20, choices=SIMNAO_CHOICES,
                                     default='Desconhecido')

    def __unicode__(self):
        return "{0}, {1}".format(self.id, format_datefield(self.data))

    class Meta:
        db_table = 'mssi_neurologico_psiquiatrico'


class MssiRenal(models.Model):
    id = models.ForeignKey(Dadosgerais, db_column='id',
                           verbose_name=DEFAULT_VALUES['verbose_id'])
    id_mssi_renal = models.AutoField(primary_key=True)
    data = models.DateField(null=True, blank=True)
    evidencia_de_disfuncao_renal = \
        models.ForeignKey('Tiposevidenciadedisfuncaorenal',
                          db_column='evidencia_de_disfuncao_renal')

    def __unicode__(self):
        return "{0}, {1}".format(self.id, format_datefield(self.data))

    class Meta:
        db_table = 'mssi_renal'


class Questionarios(models.Model):
    id = models.ForeignKey(Dadosgerais, db_column='id',
                           verbose_name=DEFAULT_VALUES['verbose_id'])
    id_questionarios = models.IntegerField(primary_key=True)
    data = models.DateField(null=True, blank=True)
    euro_qol = models.CharField(max_length=20, blank=True)
    bpi = models.CharField(max_length=20, blank=True)
    kindl = models.CharField(max_length=20, blank=True)
    outros_questionarios = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return "{0}, {1}".format(self.id, format_datefield(self.data))

    class Meta:
        db_table = 'questionarios'


class Tiposacroparestesia(models.Model):
    codigo = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=9, blank=True)

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposacroparestesia'


class TiposangioressonanciaMagnetica(models.Model):
    id_tiposangioressonancia_magnetica = models.SmallIntegerField(
        primary_key=True)
    descricao = models.CharField(max_length=100)

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposangioressonancia_magnetica'


class Tiposcerebrovascular(models.Model):
    codigo = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposcerebrovascular'


class Tiposevidenciadedisfuncaorenal(models.Model):
    codigo = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=60, blank=True)

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposevidenciadedisfuncaorenal'


class Tiposgenotipagem(models.Model):
    id_tiposgenotipagem = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposgenotipagem'


class Tiposmodificacoesnaespessuramiocardio(models.Model):
    codigo = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=255, blank=True,
                                 verbose_name='Categoria de modificacoes na \
                                 espessura do  miocardio')

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposmodificacoesnaespessuramiocardio'


class TiposreacaoPosInfusao(models.Model):
    id_tiposreacao_pos_infusao = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=100,
                                 verbose_name='Reacão pos infusão')

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposreacao_pos_infusao'
        ordering = ['descricao', ]


class TiposcondutaAReacaoPosInfusao(models.Model):
    id_tiposconduta_a_reacao_pos_infusao = \
        models.SmallIntegerField(primary_key=True)
    descricao = \
        models.CharField(max_length=100, verbose_name='Conduta a reacão pos \
        infusão')

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposconduta_a_reacao_pos_infusao'
        ordering = ['descricao', ]


class Tipossexo(models.Model):
    id_sexo = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=20)

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tipossexo'


class Tiposvertigem(models.Model):
    codigo = models.SmallIntegerField(primary_key=True)
    descricao = models.CharField(max_length=8, blank=True)

    def __unicode__(self):
        return "{0}".format(self.descricao)

    class Meta:
        db_table = 'tiposvertigem'
