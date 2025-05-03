from django import template

register = template.Library()

@register.simple_tag
def badge_class(theme_key):
    color_map = {
        'championships': 'badge-info',
        'teams_players': 'badge-primary',
        'stats_rankings': 'badge-secondary',
        'updates_news': 'badge-warning',
        'strategies': 'badge-accent',
        'skins_items': 'badge-success',
        'community_events': 'badge-error',
        'other': 'badge-neutral',
    }
    return f'badge-soft {color_map.get(theme_key, "badge-neutral")}'
