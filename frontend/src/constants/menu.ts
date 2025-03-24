import { ChatIcon } from "@/shared/icons/ChatIcon";
import { ProfileIcon } from "@/shared/icons/ProfileIcon";
import { SearchIcon } from "@/shared/icons/SearchIcon";
import { StarIcon } from "@/shared/icons/StarIcon";
import { WorkIcon } from "@/shared/icons/WorkIcon";

export const bottomMenu = [
    {
        href:'/liked',
        label:'Liked',
        icon:StarIcon
    },
    {
        href:'/search',
        label:'Search',
        icon:SearchIcon
    },
    {
        href:'/work',
        label:'Work',
        icon:WorkIcon
    },
    {
        href:'/chats',
        label:'Chats',
        icon:ChatIcon
    },
    {
        href:'/profile',
        label:'Profile',
        icon:ProfileIcon
    }
]