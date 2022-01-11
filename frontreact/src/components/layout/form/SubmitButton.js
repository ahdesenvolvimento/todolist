export default function SubmitButton({text, className}){
    return (
        <>
            <button type="submit" className={className}>{text}</button>
        </>
    )
}