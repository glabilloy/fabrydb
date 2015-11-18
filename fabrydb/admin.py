from django.contrib import admin
from fabrydb.models import (AvaliacaoCardiologica, AvaliacaoNeurologica,
                            AvaliacaoOftalmologica, AvaliacaoRenal, Banco,
                            BioquimicaGeral, DadosDaInfusao, Dadosgerais,
                            MssiCardiologico, MssiGeral,
                            MssiNeurologicoPsiquiatrico, MssiRenal,
                            Questionarios)
from fabrydb.models import (Tiposecg, TiposecocardiogramaI, Tiposholter2H,
                            Tiposacroparestesia,
                            TiposangioressonanciaMagnetica,
                            Tiposcerebrovascular,
                            Tiposevidenciadedisfuncaorenal, Tiposgenotipagem,
                            TiposmedicacoesEmUso,
                            Tiposmodificacoesnaespessuramiocardio,
                            TiposreacaoPosInfusao,
                            TiposcondutaAReacaoPosInfusao,
                            TiposresultadoDaBiopsia, Tipossexo, Tiposvertigem)

# Custom admin console
class FabrydbAdminSite(admin.AdminSite):
    site_header = 'FaBRyDB'

fadmin = FabrydbAdminSite(name='fadmin')


# Registering models
class ListEcgInline(admin.TabularInline):
    model = AvaliacaoCardiologica.category_ecg.through


class ListEcocardiogramaiInline(admin.TabularInline):
    model = AvaliacaoCardiologica.category_ecocardiogramai.through


class ListHolter2hInline(admin.TabularInline):
    model = AvaliacaoCardiologica.category_holter2h.through


class ListDadosgeraisInline(admin.TabularInline):
    model = Dadosgerais.category_medicacoes_em_uso.through


class ListAvaliacaorenalInline(admin.TabularInline):
    model = AvaliacaoRenal.category_resultados_da_biopsia.through


class AvaliacaoCardiologicaAdmin(admin.ModelAdmin):
    list_display = ['id', 'data']
    list_filter = ['category_ecg', 'id']
    search_fields = ['id__nome']
    inlines = [ListEcgInline, ListEcocardiogramaiInline, ListHolter2hInline, ]


class DadosgeraisAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_de_nascimento', 'category_genotipagem']
    list_filter = ['sexo', 'etnia', 'category_genotipagem', 'nome']
    search_fields = ['nome']
    inlines = [ListDadosgeraisInline, ]


class DadosDaInfusaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'category_reacao_pos_infusao',
                    'category_conduta_a_reacao_pos_infusao']
    list_filter = ['data', 'category_conduta_a_reacao_pos_infusao__descricao',
                   'category_reacao_pos_infusao__descricao', 'id']
    search_fields = ['id__nome']

    change_form_template = 'admin/change_computed_fields.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """Includes computed fields."""
        d = DadosDaInfusao.objects.get(pk = object_id)
        extra_context = extra_context or {}
        extra_context['infusao'] = d
        return super(DadosDaInfusaoAdmin, self).change_view(request, object_id,
            form_url, extra_context=extra_context)


class AvaliacaoRenalAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'biopsia_renal']
    list_filter = ['biopsia_renal', 'id']
    search_fields = ['id__nome']
    inlines = [ListAvaliacaorenalInline, ]


class MssiCardiologicoAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'modificacoes_na_espessura_do_miocardio']
    list_filter = ['modificacoes_na_espessura_do_miocardio',
                   'anormalidades_no_ecg', 'marcapasso', 'hipertensao', 'id']
    search_fields = ['id__nome']


class MssiRenalAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'evidencia_de_disfuncao_renal']
    list_filter = ['evidencia_de_disfuncao_renal', 'id']
    search_fields = ['id__nome']


class AvaliacaoNeurologicaAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'category_angioressonancia_magnetica']
    list_filter = ['category_angioressonancia_magnetica', 'id']
    search_fields = ['id__nome']


class AvaliacaoOftalmologicaAdmin(admin.ModelAdmin):
    list_display = ['id', 'data']
    list_filter = ['cornea_verticilata', 'tortuosidade_dos_vasos_retinianos',
                   'tortuosidade_dos_vasos_conjuntivais',
                   'opacidade_da_cornea', 'id']
    search_fields = ['id__nome']


class BioquimicaGeralAdmin(admin.ModelAdmin):
    list_display = ['id', 'data']
    list_filter = ['id']
    search_fields = ['id__nome']


class MssiGeralAdmin(admin.ModelAdmin):
    list_display = ['id', 'data']
    list_filter = ['aparencia_facial_caracteristica', 'angioqueratoma',
                   'edema', 'musculoesqueletico', 'cornea_verticilata',
                   'diaforese', 'dor_abdominal', 'diarreiaconstipacao',
                   'hemorroidas', 'pulmonar', 'nyha', 'id']
    search_fields = ['id__nome']


class MssiNeurologicoPsiquiatricoAdmin(admin.ModelAdmin):
    list_display = ['id', 'data']
    list_filter = ['vertigem', 'acroparestesia', 'crises_de_febre_e_dor',
                   'cerebrovascular', 'depressao', 'fadiga', 'hipoatividade',
                   'id']
    search_fields = ['id__nome']


fadmin.register(AvaliacaoCardiologica, AvaliacaoCardiologicaAdmin)
fadmin.register(AvaliacaoNeurologica, AvaliacaoNeurologicaAdmin)
fadmin.register(AvaliacaoOftalmologica, AvaliacaoOftalmologicaAdmin)
fadmin.register(AvaliacaoRenal, AvaliacaoRenalAdmin)
fadmin.register(Banco)
fadmin.register(BioquimicaGeral, BioquimicaGeralAdmin)
fadmin.register(DadosDaInfusao, DadosDaInfusaoAdmin)
fadmin.register(Dadosgerais, DadosgeraisAdmin)
fadmin.register(MssiCardiologico, MssiCardiologicoAdmin)
fadmin.register(MssiGeral, MssiGeralAdmin)
fadmin.register(MssiNeurologicoPsiquiatrico,
                    MssiNeurologicoPsiquiatricoAdmin)
fadmin.register(MssiRenal, MssiRenalAdmin)
fadmin.register(Questionarios)

fadmin.register(Tiposecg)
fadmin.register(TiposecocardiogramaI)
fadmin.register(Tiposholter2H)
fadmin.register(Tiposacroparestesia)
fadmin.register(TiposangioressonanciaMagnetica)
fadmin.register(Tiposcerebrovascular)
fadmin.register(Tiposevidenciadedisfuncaorenal)
fadmin.register(Tiposgenotipagem)
fadmin.register(TiposmedicacoesEmUso)
fadmin.register(Tiposmodificacoesnaespessuramiocardio)
fadmin.register(TiposreacaoPosInfusao)
fadmin.register(TiposcondutaAReacaoPosInfusao)
fadmin.register(TiposresultadoDaBiopsia)
fadmin.register(Tipossexo)
fadmin.register(Tiposvertigem)





admin.site.register(AvaliacaoCardiologica, AvaliacaoCardiologicaAdmin)
admin.site.register(AvaliacaoNeurologica, AvaliacaoNeurologicaAdmin)
admin.site.register(AvaliacaoOftalmologica, AvaliacaoOftalmologicaAdmin)
admin.site.register(AvaliacaoRenal, AvaliacaoRenalAdmin)
admin.site.register(Banco)
admin.site.register(BioquimicaGeral, BioquimicaGeralAdmin)
admin.site.register(DadosDaInfusao, DadosDaInfusaoAdmin)
admin.site.register(Dadosgerais, DadosgeraisAdmin)
admin.site.register(MssiCardiologico, MssiCardiologicoAdmin)
admin.site.register(MssiGeral, MssiGeralAdmin)
admin.site.register(MssiNeurologicoPsiquiatrico,
                    MssiNeurologicoPsiquiatricoAdmin)
admin.site.register(MssiRenal, MssiRenalAdmin)
admin.site.register(Questionarios)

admin.site.register(Tiposecg)
admin.site.register(TiposecocardiogramaI)
admin.site.register(Tiposholter2H)
admin.site.register(Tiposacroparestesia)
admin.site.register(TiposangioressonanciaMagnetica)
admin.site.register(Tiposcerebrovascular)
admin.site.register(Tiposevidenciadedisfuncaorenal)
admin.site.register(Tiposgenotipagem)
admin.site.register(TiposmedicacoesEmUso)
admin.site.register(Tiposmodificacoesnaespessuramiocardio)
admin.site.register(TiposreacaoPosInfusao)
admin.site.register(TiposcondutaAReacaoPosInfusao)
admin.site.register(TiposresultadoDaBiopsia)
admin.site.register(Tipossexo)
admin.site.register(Tiposvertigem)
