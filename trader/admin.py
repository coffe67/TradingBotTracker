from django.contrib import admin

from .models import TradeAlert, SymbolPrice


@admin.register(TradeAlert)
class TradeAlertAdmin(admin.ModelAdmin):
    list_display = ("symbol", "trade_price", "kind", "is_active", "created")


@admin.register(SymbolPrice)
class SymbolPriceAdmin(admin.ModelAdmin):
    list_display = ("symbol", "price", "created")
