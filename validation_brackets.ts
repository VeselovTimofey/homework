function validation_string(string_of_brackets: string): boolean
{
    if (string_of_brackets == '')
    // checking for an empty string.
    {
        return false;
    }
    let answer: boolean = true;
    type Element_Counter =
    {
        '(': number,
        '[': number,
        '{': number
    };
    type Double =
    {
        ')': string,
        ']': string,
        '}': string
    };
    var element_counter: Element_Counter = {'(': 0, '[': 0, '{': 0}
    var double: Double = {')': '(', ']': '[', '}': '{'};
    let element: string;
    for (element of string_of_brackets)
    {
        if (element in element_counter)
        {
            element_counter[element as keyof Element_Counter] = element_counter[element as keyof Element_Counter] + 1;
        }
        else if (element in double && element_counter[double[element as keyof Double] as keyof Element_Counter] > 0)
        // checking that the element is a right bracket and has a pair
        {
            element_counter[double[element as keyof Double] as keyof Element_Counter] = element_counter[double[element as keyof Double] as keyof Element_Counter] - 1;
        }
        else
         // if there is something other than bracket, exit the loop
         {
            element_counter['('] = element_counter['('] + 1;
            break
         }
    }
    let count: any;
    for (count in element_counter)
     // checking that we don't have brackets without a pair
     {
        if (element_counter[count as keyof Element_Counter] != 0)
        {
            answer = false;
            break;
        }
     }
    return answer;
}

console.log(validation_string('[{(()])}'));
