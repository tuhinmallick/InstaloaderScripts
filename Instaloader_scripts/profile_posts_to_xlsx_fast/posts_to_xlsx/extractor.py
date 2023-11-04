def post_to_dict(post):
    return {
        "owner_username": post.owner_username,
        "owner_id": post.owner_id,
        "post_date": post.date_utc,
        "post_caption": post.caption,
        "tagged_users": post.tagged_users,
        "caption_mentions": post.caption_mentions,
        "is_video": post.is_video,
        "video_view_count": post.video_view_count,
        "video_duration": post.video_duration,
        "likes": post.likes,
        "comments": post.comments,
        "post_url": f"https://www.instagram.com/p/{post.shortcode}",
        "hashtags_caption": post.caption_hashtags,
    }
