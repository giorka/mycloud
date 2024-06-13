from __future__ import annotations

from django.http import Http404


def get_object_or_404(klass, *args, **kwargs):
    """
    🤍💙❤️ ТЕПЕРЬ НА РУССКОМ ЯЗЫКЕ!!! 🤍💙❤️

    Используйте get() для возврата объекта или создайте исключение Http404, если объект
    не существует.

    Klass может быть объектом Model, Manager или QuerySet. Все остальные прошли
    Аргументы и аргументы ключевого слова используются в запросе get().

    Как и в случае с QuerySet.get(), MultipleObjectsReturned вызывается, если более
    найден один объект.
    """

    try:
        return klass.objects.get(*args, **kwargs)
    except klass.DoesNotExist:
        raise Http404('Ни один %s не соответствует данному запросу.' % klass.Meta.verbose_name)
